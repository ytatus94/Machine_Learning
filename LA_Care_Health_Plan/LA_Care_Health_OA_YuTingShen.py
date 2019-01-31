#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Calculate sensitivity and specificity of the model
def calculate_sensitivity_and_specificity(df, threshold):
    P, N, TP, TN, FP, FN = 0, 0, 0, 0, 0, 0

    for index, row in df.iterrows():
        if row['class'] == 1: # Ground Truth Positive
            P += 1
            if row['predicted_prob'] >= threshold: # Predicted Positive
                TP += 1
            else: # Predicted Negative
                FN += 1
        else: # Ground Truth Negative
            N += 1
            if row['predicted_prob'] < threshold: # Predicted Negative
                TN += 1
            else: # Predicted Positive
                FP += 1

    tpr = TP/P
    tnr = TN/N
    
    return tpr, tnr

# Calculate AUC
def calculate_auc(df):
    # Sort df by the predicted_prob column using descending order
    df_sorted = df.sort_values(by='predicted_prob', ascending=False)
    
    y_true = df_sorted['class'].values
    y_score = df_sorted['predicted_prob'].values

    index = np.arange(len(y_score))
    
    # Calculate the true positives and false positives
    tps = np.cumsum(y_true)
    fps = (index + 1) - tps

    # Calculate the true positive rates and false positives
    tpr = tps / tps[-1]
    fpr = fps / fps[-1]

    area = np.trapz(tpr, fpr)
    
    return fpr, tpr, area

# Plot ROC curve
def plot_roc_curve(fpr, tpr, area):
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', linewidth=2, label='ROC curve (area = %0.4f)' % area)
    plt.plot([0, 1], [0, 1], color='navy', linewidth=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()

def main():
	df = pd.read_csv('model_outcome.csv')

	tpr, tnr = calculate_sensitivity_and_specificity(df, 0.5)
	print('Sensitivity (TPR) = %.4f, specificity (TNR) = %.4f' % (tpr, tnr))
	
	fpr, tpr, area = calculate_auc(df)
	print('AUC = %.4f' % area)
	
	plot_roc_curve(fpr, tpr, area)

if __name__ == '__main__':
	main()