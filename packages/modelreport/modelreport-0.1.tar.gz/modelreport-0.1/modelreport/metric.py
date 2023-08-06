from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,f1_score,roc_curve, auc,recall_score,matthews_corrcoef,cohen_kappa_score
import pandas as pd

class evaluationreport:
    def __init__(self,y_test, y_pred):
        self.y_test=y_test
        self.y_pred=y_pred

    def find_accuracy_score(self):
        try:
            return accuracy_score(self.y_test, self.y_pred)
        except Exception as e:
            return e
        
    def find_confusion_matrix(self):
        try:
            return confusion_matrix(self.y_test, self.y_pred)
        except Exception as e:
            return e
        
    def find_precision_score(self):
        try:
            return precision_score(self.y_test, self.y_pred)
        except Exception as e:
            return e

    def find_recall_score(self):
        try:
            return recall_score(self.y_test, self.y_pred)
        except Exception as e:
            return e

    def find_f1_score(self):
        try:
            return f1_score(self.y_test, self.y_pred)
        except Exception as e:
            return e
        
    def find_auc_score(self):
        try:
            fpr, tpr, threshold = roc_curve(self.y_test, self.y_pred)
            return auc(fpr, tpr)
        except Exception as e:
            return e
        
    def find_matthews_corrcoef(self):
        try:
            return matthews_corrcoef(self.y_test, self.y_pred)
        except Exception as e:
            return e

    def find_cohen_kappa_score(self):
        try:
            return cohen_kappa_score(self.y_test, self.y_pred)
        except Exception as e:
            return e 
        
    def evaluationreport(self):
        try:
            metrics_ls=['Accuracy','Precision','Recall','f1_score','AUC_score','matthews_corrcoef','cohen_kappa_score','confusion_matrix']
            score_ls=[self.find_accuracy_score(),self.find_precision_score(),self.find_recall_score(),self.find_f1_score(),self.find_auc_score(),self.find_matthews_corrcoef(),self.find_cohen_kappa_score(),self.find_confusion_matrix()]
            df = pd.DataFrame(list(zip(metrics_ls, score_ls)),columns =['Metrics','Score'])
            return df        
        except Exception as e:
            return e 

# if __name__ == '__main__':        
#     y_test=[1,0,0,0,0,1,1,1,0]
#     y_pred=[1,0,0,1,1,0,0,1,1]
#     ev=evaluationreport()
#     print(ev.evaluationreport(y_test,y_pred))

def result_summary(y_test,y_pred):
    try:
        if len(y_test)==len(y_pred):
            ev=evaluationreport(y_test,y_pred)         
            return ev.evaluationreport()
        else:
            ev=evaluationreport(y_test,y_pred)         
            return ev.find_accuracy_score()
    except Exception as e:
        return e

