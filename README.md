# SAD

Projekt został zrealizowany w ramach kursu Statystyczna Analiza Danych (semestr letni 2024/2025). Jego celem było przewidywanie ilości białka powierzchniowego CD36 w komórkach układu immunologicznego na podstawie danych RNA pochodzących z wielomodalnego sekwencjonowania pojedynczych komórek (scRNA-seq).

Na początku przeprowadzono eksploracyjną analizę danych, obejmującą m.in. sprawdzenie typów zmiennych, ich wstępne przekształcenie oraz ocenę kompletności zbioru. Następnie zastosowano narzędzia statystyczne, takie jak wykresy Q-Q, heatmapy, wykresy wiolinowe i pudełkowe, a także przeprowadzono testy statystyczne w języku R. Na ich podstawie formułowano hipotezy zerowe, które następnie były weryfikowane przy użyciu odpowiednich metod statystycznych.

W dalszej części projektu analizowano model ElasticNet, poszukując optymalnych hiperparametrów z wykorzystaniem walidacji krzyżowej. Wyniki porównano z modelami alternatywnymi: lasem losowym oraz modelem referencyjnym, przypisującym średnią wartość zmiennej objaśnianej.

W ostatnim etapie opracowano model predykcyjny, który estymował poziom białka CD36 na podstawie dostarczonych danych treningowych. Wyniki końcowe zostały zgłoszone na platformie Kaggle, gdzie udostępniono mechanizm oceny jakości predykcji.

Każdy folder w repozytorium zawiera kod źródłowy oraz szczegółowy opis zastosowanych metod i otrzymanych rezultatów. Projekt został zrealizowany w językach R i Python

English-version:

This project was completed as part of the Statistical Data Analysis course (summer semester 2024/2025). The goal was to predict the abundance of the surface protein CD36 in immune system cells based on RNA data obtained through multimodal single-cell RNA sequencing (scRNA-seq).

The project began with exploratory data analysis, including inspection and preprocessing of variable types, checking data completeness, and performing initial transformations. Various statistical tools were then applied — including Q-Q plots, heatmaps, violin plots, and boxplots — followed by statistical hypothesis testing using R. Null hypotheses were formulated based on the visualizations and tested using appropriate statistical methods.

The next stage focused on the ElasticNet regression model. A grid search combined with cross-validation was used to identify optimal hyperparameters. The ElasticNet model's performance was then compared to alternative approaches: Random Forest and a reference model assigning the mean of the target variable.

In the final step, a predictive model was built to estimate CD36 protein levels based on the provided training data. The predictions were submitted to Kaggle, where an automatic leaderboard was used to evaluate model performance.

Each folder in this repository contains source code and a detailed description of the methods used and the results obtained. The project was implemented using both R and Python.