import cv2, time
from .person_detection_trt import PersonDetectionTrt
from ..model_zoo import BYTETracker


class PersonReidTrt:
    def __init__(self,
                 model_file='models/bytetrack_x_fp16.trt',
                 score_thr=0.2,
                 nms_thr=0.7,
                 track_thresh=0.5,
                 match_thresh=0.8,
                 track_buffer=30,
                 frame_rate=30,
                 person_detector=None,
                 person_reid=None):
        if person_detector is None:
            self.detector = PersonDetectionTrt(model_file, score_thr, nms_thr)
        else:
            self.detector = person_detector
        self.tracker = BYTETracker(track_thresh, match_thresh, track_buffer, frame_rate)
        self.reid = person_reid
        self.person_id = {}

    def predict(self, image, min_box_area=10, aspect_ratio_thresh=1.6, match_thresh=0.87):
        img_info = image.shape[:2]
        results = []
        outputs = self.detector.predict(image)
        if outputs is not None:
            targets = self.tracker.update(outputs, img_info, img_info)
            for t in targets:
                vertical = t.tlwh[2] / t.tlwh[3] > aspect_ratio_thresh
                if t.tlwh[2] * t.tlwh[3] > min_box_area and not vertical:
                    name = 'OT_' + str(t).split('_')[1]
                    box = list(t.tlwh.astype(int))
                    _l, _t, _r, _b = max(box[0], 0), max(box[1], 0), min(box[0] + box[2] - 1, img_info[1] - 1), \
                                     min(box[1] + int(0.9 * box[3]), img_info[0] - 1)
                    img_crop = image[_t:_b + 1, _l:_r + 1][:, :, ::-1]
                    feat = self.reid.predict(img_crop)

                    if name not in self.person_id:
                        # 检索
                        idx, score = self.reid.index(feat, recall_num=1)
                        if int(idx[0]) == -1 or float(score[0]) < match_thresh:
                            m = 'not match'
                            self.person_id[name] = t.track_id
                        else:
                            m = 'match'
                            self.person_id[name] = int(self.reid.query_names[idx])
                        cv2.imwrite("{}_{}_{}_{}_{}.png".format(name,
                                                                str(self.person_id[name]),
                                                                str(idx[0]),
                                                                str(score[0]),
                                                                m),
                                    img_crop[:, :, ::-1])
                    if t.score > 0.35:
                        self.reid.update_features(self.person_id[name], self.person_id[name], feat)

                    results.append(dict(box=list(t.tlwh.astype(int)),
                                        id=self.person_id[name],
                                        score=t.score))
        return results

    def show(self, image, results):
        h, w = image.shape[:2]
        for result in results:
            box = result['box']
            l, t, r, b = max(box[0], 0), max(box[1], 0), min(box[0] + box[2] - 1, w - 1), \
                         min(box[1] + int(0.9 * box[3]), h - 1)
            cv2.rectangle(image, (l, t), (r, b), (255, 0, 255), 2)
            cv2.putText(image, 'id: %d, score: %.2f' % (result['id'], result['score']),
                        (l, max(t - 4, 0)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), thickness=2)
        return image

    def predict_video(self, file_path=0, min_box_area=10, aspect_ratio_thresh=1.6):
        cap = cv2.VideoCapture(file_path)
        frame_id = 0
        while True:
            ret, frame = cap.read()
            if ret:
                s = time.time()
                results = self.predict(frame, min_box_area, aspect_ratio_thresh)
                print("person nums: ", len(results), time.time() - s)
                if len(results) > 0:
                    frame = self.show(frame, results)
                    cv2.imwrite('/home/cash/WorkSpace/online_data/results/' + str(frame_id) + '.jpg', frame)
            else:
                break
            frame_id += 1
