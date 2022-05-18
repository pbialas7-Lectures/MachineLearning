import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted

from sklearn.mixture import GaussianMixture
from scipy.stats import multivariate_normal



class GaussianMixtureDiscriminantAnalysis(BaseEstimator, ClassifierMixin):
    def __init__(self, n_cmp = (2,2) , tol=1e-4 , max_iter=100 ):
        super().__init__()
        self.n_cmp = n_cmp
        self.tol = tol
        self.max_iter = max_iter

    def fit(self, X, y):
        self.X_, self.y_ = check_X_y(X, y)
        self.cls_ = [GaussianMixture(n_components=n_cmp, tol=self.tol, max_iter=self.max_iter) for n_cmp in self.n_cmp]
    
        for l, cmp in enumerate(self.cls_):
                cmp.fit(self.X_[self.y_==l])
        
        self.means_ = [cmp.means_ for cmp in self.cls_]
        self.covs_  = [cmp.covariances_ for cmp in self.cls_]
        self.pdfs_ = [[multivariate_normal(cmp.means_[i], cmp.covariances_[i]).pdf for i in range(cmp.n_components)] for cmp in self.cls_]
        
        return self  
    
    def predict_proba(self, X):
        check_is_fitted(self)
        p = np.zeros((len(X),2) )
        for k,cmp in enumerate(self.cls_):
            for i in range(cmp.n_components):
                p[:,k]+= cmp.weights_[i]*self.pdfs_[k][i](X)
        
        proba = p[:,0]/p.sum(1)     
        return  np.stack((proba, 1-proba),axis=1)
        
    def predict(self, X):
        X = check_array(X)
        return (self.predict_proba(X)>0.5).astype('int64')
    