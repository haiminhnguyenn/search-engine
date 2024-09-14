from PIL import Image
from pathlib import Path
import numpy as np

from feature_extractor import FeatureExtractor

if __name__ == '__main__':
    fe = FeatureExtractor()
    for img_path in sorted(Path("./static/reverse_img_store").glob("*.jpg")):

        feature = fe.extract(img = Image.open(img_path))
        #Save the Features
        feature_path = Path("./static/feature") / (img_path.stem + ".npy")
        np.save(feature_path, feature)