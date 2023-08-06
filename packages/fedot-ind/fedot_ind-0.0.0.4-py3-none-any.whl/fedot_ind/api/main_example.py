from fedot_ind.api.main import FedotIndustrial

if __name__ == "__main__":
    import os.path
    from fedot_ind.core.architecture.postprocessing.results_picker import ResultsPicker

    datasets = ['ItalyPowerDemand',
                'UMD'
                ]

    for dataset_name in datasets:

        industrial = FedotIndustrial(task='ts_classification',
                                     dataset=dataset_name,
                                     strategy='fedot_preset',
                                     # strategy='statistical',
                                     # strategy='wavelet',
                                     use_cache=True,
                                     timeout=1,
                                     n_jobs=2,
                                     window_sizes='auto',
                                     logging_level=20,
                                     output_folder=None)

        train_data, test_data, _ = industrial.reader.read(dataset_name=dataset_name)
        model = industrial.fit(train_features=train_data[0], train_target=train_data[1])

        labels = industrial.predict(test_features=test_data[0],
                                    test_target=test_data[1])

        probs = industrial.predict_proba(test_features=test_data[0],
                                         test_target=test_data[1])
        metric = industrial.get_metrics(target=test_data[1],
                                        metric_names=['f1', 'roc_auc'])

        for pred, kind in zip([labels, probs], ['labels', 'probs']):
            industrial.save_predict(predicted_data=pred, kind=kind)

        industrial.save_metrics(metrics=metric)

    results_path = os.path.abspath('../../results_of_experiments')
    picker = ResultsPicker(path=results_path)
    proba_dict, metric_dict = picker.run()
    from fedot_ind.core.ensemble.static.RankEnsembler import RankEnsemble

    ensembler = RankEnsemble(dataset_name='ItalyPowerDemand',
                             proba_dict=proba_dict,
                             metric_dict=metric_dict)
    ensembler.ensemble()
