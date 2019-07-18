import pandas as pd
import numpy as np
import collections

# dict structure: allClasses_dict (holds results for each class) -> metric_scores (holds many key_vals with all metrics and scores) 
def calc_bootstrap(bootstrap, WYT):
	allClasses_dict = {}
	for currentClass, gages in bootstrap.items():
		'''combine all the items in the gages list () to get a single object with all observations'''
		for index, gage in enumerate(gages):
			if index == 0:
				all_gages = gage
			else:
				all_gages = all_gages.append(gage)
		all_gages = all_gages.reset_index()
		metrics = all_gages.columns.values.tolist()[2:-1] 
		sample_num = round(len(all_gages)/10)
		metric_scores = collections.OrderedDict()
		for metric in metrics:
			'''Calculate scores many iterations and take average of the results'''
			iters = 10
			score1090 = []
			score = []
			o_e = []
			train_avg = []
			test_avg = []
			for index in range(iters):
				test = []
				train = []
				'''randomly select a 10% test subset for removal'''
				sample = all_gages.sample(n=int(sample_num), random_state=1).index
				for i in sample.values:
					test.append(all_gages.iloc[i])
				for i in range(len(all_gages)):
					if i in sample.values:
						continue
					else:
						train.append(all_gages.iloc[i])
				train_vals = []
				test_vals = []
				for i in range(len(train)):
					train_vals.append(train[i][metric])
				for i in range(len(test)):
					test_vals.append(test[i][metric])
				'''calculate upper and lower train bounds to compare against test'''
				low_train = np.nanpercentile(train_vals, 0)
				high_train = np.nanpercentile(train_vals, 100)
				low_train2 = np.nanpercentile(train_vals, 10)
				high_train2 = np.nanpercentile(train_vals, 90)
				count = 0
				count2 = 0
				'''keep track of when test val goes outside train bounds, use final count as a score'''
				for i in range(len(test)):
					if currentClass == 'class5':
						import pdb; pdb.set_trace()
					if test[i][metric] < low_train or test[i][metric] > high_train:
						count += 1
					if test[i][metric] < low_train2 or test[i][metric] > high_train2:
						count2 += 1
				'''assemble results from each iteration into list'''
				score1090.append((float(count2)/float(len(test))))
				score.append(float(count)/float(len(test)))
				o_e.append(np.nanmean(train_vals)/np.nanmean(test_vals))
				train_avg.append(np.nanmean(train_vals))
				test_avg.append(np.nanmean(test_vals))
			'''final output is average scores from all iterations'''
			metric_scores[metric+'_score1090'] = np.nanmean(score1090)
			metric_scores[metric+'_score'] = np.nanmean(score)
			metric_scores[metric+'_o/e'] = np.nanmean(o_e)
			metric_scores[metric+'_train_avg'] = np.nanmean(train_avg)
			metric_scores[metric+'_test_avg'] = np.nanmean(test_avg)
		'''assemble dict of scores for each class into final dict holding all class results'''
		allClasses_dict[currentClass] = metric_scores
	return allClasses_dict, metrics, WYT
