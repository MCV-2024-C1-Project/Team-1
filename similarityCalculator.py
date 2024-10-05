import cv2
import numpy as np

class SimilarityCalculator:
    METHODS = (
        ("CORREL", cv2.HISTCMP_CORREL),
        ("CHISQR", cv2.HISTCMP_CHISQR),
        ("INTRSC", cv2.HISTCMP_INTERSECT),
        ("HELLGR", cv2.HISTCMP_BHATTACHARYYA),
    )

    methods_dict = {name: method for name, method in METHODS}

    def compute_similarity(self, hist_in, hist_ref, method_name="CHISQR"):
        """Function to compute the similarity between histograms.

        Args:
            hist_in (list): histograms of query images.
            hist_ref (list): histograms of reference images.
            method_name (str, optional): similarity metric to apply ('CORREL', 'CHISQR', 'INTRSC', 'HELLGR'). Defaults to "CHISQR".

        Raises:
            ValueError: If method name is not valid.

        Returns:
            numpy.ndarray: similarity matrix s[n,m], where n is the number of inputs and m is the number of reference histograms. s[i,j] shows the similarity between input i and reference j. 
        """
        if method_name not in self.methods_dict:
            raise ValueError(f"Invalid method name '{method_name}'.\nValid options: {list(self.methods_dict.keys())}")
        self.method = self.methods_dict[method_name]
        self.hist_in = hist_in
        self.hist_ref = hist_ref
        
        sim_results = []
        for h_in in self.hist_in:
            sim_results_per_img = []
            for h_ref in self.hist_ref:
                sim_results_per_img.append(cv2.compareHist(h_in, h_ref, self.method))
            sim_results.append(sim_results_per_img)
        return np.array(sim_results)
