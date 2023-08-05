import shap

from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier as XGBC
from xgboost import XGBRegressor as XGBR
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm

class feature_selection:

    def __init__(self,verbose=True,type=1):

   
        self.verbose=verbose
        self.x=None
        self.result=None
        self.shapely_value=None
        self.type=type
        self.model=None
        self.feature_ranking=None


    def fit(self,x,y,alpha=0.8):
        self.x=x


        if self.verbose:
            print("Preprocessing data...")

        x=StandardScaler().fit_transform(x)

        if self.verbose:
            print("Model training...")

        self.ml()
        self.model.fit(x,y)

        if self.verbose:
            print("Computing explanations...")

        explainer=shap.TreeExplainer(self.model)
        shap_values=explainer.shap_values(x)

        self.shapely_value=shap_values

        if self.verbose:
            print("Features selecting...")

        self.selection_rule(alpha)



    def selection_rule(self,alpha=0.8):
        x=self.x
        self.feature_ranking=pd.DataFrame(zip(np.abs(self.shapely_value).sum(0),x.columns),columns=["Shapely","Features name"],index=range(len(x.columns)))
        self.feature_ranking.sort_values(["Shapely"] , inplace=True, ascending=False)
        self.feature_ranking.index=range(len(x.columns))
        
        sum=0
        result=[]

        for i,n in enumerate(self.feature_ranking["Shapely"].tolist()):

            if sum/np.sum(self.feature_ranking["Shapely"].tolist())<alpha:
                sum+=n
                result.append(self.feature_ranking["Features name"][i])

        self.result=result
        print(self.result)


    def feature_importance_plot(self):


        x = np.arange(0, 12, step=.5)

        y = np.sqrt(x)

        norm = plt.Normalize(y.min(), y.max())

        norm_y = norm(y)
        map_vir = cm.get_cmap(name='GnBu')
        color = map_vir(norm_y)


        plt.figure(figsize=(10,5),dpi=300)


        plt.bar(self.feature_ranking["Features name"],self.feature_ranking["Shapely"],color=color[::-1])

        plt.xticks(rotation = 40,fontsize=7,c="black")

        plt.yticks(fontsize=7)

        plt.ylabel("Features importance")

        plt.yticks()
        plt.show()
        

    def ml(self):

        if self.type==1:

            self.model=XGBR(max_depth=4, learning_rate=0.05, n_estimators=200)
        
        elif self.type==0:

            self.model=XGBC(learning_rate =0.025,n_estimators=200,max_depth=3,min_child_weight=9,colsample_bylevel=0.4,gamma=0.5)
        
        else:
            print("Please enter 0 or 1 for the classification model and regression model")




    def feature_beeswarm(self, color_polyline='black',
                    alpha_polyline=0.1, max_display=30, order_p=shap.Explanation.abs.mean(0),
                clustering=None, cluster_threshold=0.5, color=None,
                axis_color="#333333", alpha=1, show=True, log_scale=False,
                color_bar=True, plot_size="auto"):
        """Create a SHAP beeswarm plot, colored by feature values when they are provided.

        Attention: This is an adaptation from the original SHAP beeswarm plot. 
        <https://github.com/slundberg/shap/blob/master/shap/plots/_beeswarm.py>
        Here, we use polylines to investigate the SHAP values for the clustering assignments.

        Parameters
        ----------
        klass : int
            The clustering label
        shap_values : np.array
            This is a (k, n, m) matrix with SHAP values
        data : np.array
            The matrix used for explanation
        cluster_labels : np.array
            The respective clustering labels for "data"
        max_display : int
            How many top features to include in the plot (default is 20, or 7 for interaction plots)
        plot_size : "auto" (default), float, (float, float), or None
            What size to make the plot. By default the size is auto-scaled based on the number of
            features that are being displayed. Passing a single float will cause each row to be that 
            many inches high. Passing a pair of floats will scale the plot by that
            number of inches. If None is passed then the size of the current figure will be left
            unchanged.

        """
        shap_values=self.shapely_value
        data=self.x
        cluster_labels=0
        feature_names=self.x.columns
        color=plt.get_cmap("RdYlGn")

        values = shap_values
        feature_order = shap.plots._utils.convert_ordering(shap.Explanation.abs.mean(0), values)
        order = shap.plots._utils.convert_ordering(order_p, values)

        num_features = min(max_display, values.shape[1])
        values[:,feature_order[num_features-1]] = np.sum([values[:,feature_order[i]] for i in 
                                                        range(num_features-1, len(values[0]))], 0)

        values_ord = values[:, order]
        indices = np.arange(num_features).astype(int)[::-1]
        # for i in range(values_ord.shape[0]):
        #     plt.plot(values_ord[i][:num_features], indices, color=color_polyline, alpha=alpha_polyline)

        c_exp = shap.Explanation(shap_values, data=data, feature_names=feature_names)
        shap.plots.beeswarm(c_exp, max_display=num_features, order=order_p,
                clustering=clustering, cluster_threshold=cluster_threshold, color=color,
                axis_color=axis_color, alpha=alpha, log_scale=log_scale,
                color_bar=color_bar, plot_size=plot_size, show=False)