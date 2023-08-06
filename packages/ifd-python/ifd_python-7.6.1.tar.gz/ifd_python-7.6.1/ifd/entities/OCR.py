from .Abstract import ADetection

class OCR(ADetection):
    score_ocr: float
    label_ocr: str
    score_match: float

    def serialize(self):
        data = super().serialize()
        data["label_ocr"] = self.label_ocr
        data["score_match"] = self.score_match
        return data
        
    def deserialize(self, data):
        super().deserialize(data)

        for field in data:
            if data[field] is None:
                pass
            elif field == "label_ocr":
                self.label_ocr = data[field]
            elif field == "score_match":
                self.score_match = data[field]
        return self