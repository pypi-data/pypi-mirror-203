<a href="https://github.com/WenjieDu/PyPOTS"><img src="https://raw.githubusercontent.com/WenjieDu/PyPOTS/main/docs/figs/PyPOTS%20logo.svg?sanitize=true" width="200" align="right"></a>

## <p align="center">Welcome to PyPOTS</p>
**<p align="center">A Python Toolbox for Data Mining on Partially-Observed Time Series</p>**

<p align="center">
    <img alt="Python version" src="https://img.shields.io/badge/Python->v3.6-yellow?color=88ada6">
    <img alt="powered by Pytorch" src="https://img.shields.io/static/v1?label=PyTorch&message=%E2%9D%A4%EF%B8%8F&color=bbcdc5&logo=pytorch">
    <a href="https://pypi.org/project/">
        <img alt="the latest release version" src="https://img.shields.io/github/v/release/wenjiedu/pypots?color=e0eee8&include_prereleases&label=Release">
    </a>
    <a href="https://github.com/WenjieDu/PyPOTS/blob/main/LICENSE">
        <img alt="GPL3 license" src="https://img.shields.io/badge/License-GPL--v3-c0ebd7">
    </a>
    <a href="https://join.slack.com/t/pypots-dev/shared_invite/zt-1gq6ufwsi-p0OZdW~e9UW_IA4_f1OfxA"> 
        <img alt="Slack Workspace" src="https://img.shields.io/badge/Slack-PyPOTS-grey?logo=slack&color=7bcfa6">
    </a>
    <a href="https://github.com/sponsors/WenjieDu">
        <img alt="GitHub Sponsors" src="https://img.shields.io/github/sponsors/wenjiedu?label=Sponsors&color=7fecad&logo=githubsponsors">
    </a>
    <a href="https://github.com/WenjieDu/PyPOTS/stargazers">
        <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/wenjiedu/pypots?logo=Github&color=7bcfa6&label=Stars">
    </a>
    <a href="https://github.com/WenjieDu/PyPOTS/forks">
        <img alt="GitHub Repo forks" src="https://img.shields.io/github/forks/wenjiedu/pypots?logo=Github&color=2edfa3&label=Forks">
    </a>
    <a href="https://github.com/WenjieDu/PyPOTS">
        <img alt="Repo size" src="https://img.shields.io/github/repo-size/WenjieDu/PyPOTS?color=25f8cb&label=Repo%20Size&logo=Github">
    </a>
    <a href="https://coveralls.io/github/WenjieDu/PyPOTS"> 
        <img alt="Coveralls coverage" src="https://img.shields.io/coverallsCoverage/github/WenjieDu/PyPOTS?branch=main&logo=coveralls&color=00e09e&label=Coverage">
    </a>
    <a href="https://anaconda.org/conda-forge/pypots">
        <img alt="Conda downloads" src="https://img.shields.io/conda/dn/conda-forge/pypots?label=Conda%20Downloads&color=48c0a3">
    </a>
    <a href="https://pypi.org/project/pypots">
        <img alt="PyPI downloads" src="https://static.pepy.tech/personalized-badge/pypots?period=total&units=international_system&left_color=grey&right_color=teal&left_text=PyPI%20Downloads">
    </a>
    <a href="https://github.com/WenjieDu/PyPOTS/actions/workflows/testing.yml"> 
        <img alt="GitHub Testing" src="https://github.com/WenjieDu/PyPOTS/actions/workflows/testing.yml/badge.svg">
    </a>
    <a href="https://doi.org/10.5281/zenodo.6823221">
        <img alt="Zenodo DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.6823221.svg">
    </a>
</p>

⦿ `Motivation`: Due to all kinds of reasons like failure of collection sensors, communication error, and unexpected malfunction, missing values are common to see in time series from the real-world environment. This makes partially-observed time series (POTS) a pervasive problem in open-world modeling and prevents advanced data analysis. Although this problem is important, the area of data mining on POTS still lacks a dedicated toolkit. PyPOTS is created to fill in this blank.

⦿ `Mission`: PyPOTS is born to become a handy toolbox that is going to make data mining on POTS easy rather than tedious, to help engineers and researchers focus more on the core problems in their hands rather than on how to deal with the missing parts in their data. PyPOTS will keep integrating classical and the latest state-of-the-art data mining algorithms for partially-observed multivariate time series. For sure, besides various algorithms, PyPOTS is going to have unified APIs together with detailed documentation and interactive examples across algorithms as tutorials.

<a href="https://github.com/WenjieDu/TSDB"><img src="https://raw.githubusercontent.com/WenjieDu/TSDB/main/docs/figs/TSDB%20logo.svg?sanitize=true" align="left" width="160"/></a>
To make various open-source time-series datasets readily available to our users, PyPOTS gets supported by project [TSDB (Time-Series DataBase)](https://github.com/WenjieDu/TSDB), a toolbox making loading time-series datasets super easy! 

Visit [TSDB](https://github.com/WenjieDu/TSDB) right now to know more about this handy tool 🛠! It now supports a total of 119 open-source datasets.
<br clear="left">

## ❖ Installation
PyPOTS now is available on <a href="https://anaconda.org/conda-forge/pypots"><img alt="on Anaconda" align="center" 
src="https://img.shields.io/badge/Anaconda--lightgreen?style=social&logo=anaconda"></a>❗️ 

Install it with `conda install pypots`, you may need to specify the channel with option `-c conda-forge`

Install the latest release from PyPI:
> pip install pypots

or install from the source code with the latest features not officially released in a version:
> pip install https://github.com/WenjieDu/PyPOTS/archive/main.zip

<details open>
<summary><b>Below is an example applying SAITS in PyPOTS to impute missing values in the dataset PhysioNet2012:</b></summary>

``` python
import numpy as np
from sklearn.preprocessing import StandardScaler
from pypots.data import load_specific_dataset, mcar, masked_fill
from pypots.imputation import SAITS
from pypots.utils.metrics import cal_mae
# Data preprocessing. Tedious, but PyPOTS can help. 🤓
data = load_specific_dataset('physionet_2012')  # PyPOTS will automatically download and extract it.
X = data['X']
num_samples = len(X['RecordID'].unique())
X = X.drop('RecordID', axis = 1)
X = StandardScaler().fit_transform(X.to_numpy())
X = X.reshape(num_samples, 48, -1)
X_intact, X, missing_mask, indicating_mask = mcar(X, 0.1) # hold out 10% observed values as ground truth
X = masked_fill(X, 1 - missing_mask, np.nan)
dataset = {"X": X}
# Model training. This is PyPOTS showtime. 💪
saits = SAITS(n_steps=48, n_features=37, n_layers=2, d_model=256, d_inner=128, n_head=4, d_k=64, d_v=64, dropout=0.1, epochs=10)
saits.fit(dataset)  # train the model. Here I use the whole dataset as the training set, because ground truth is not visible to the model.
imputation = saits.impute(dataset)  # impute the originally-missing values and artificially-missing values
mae = cal_mae(imputation, X_intact, indicating_mask)  # calculate mean absolute error on the ground truth (artificially-missing values)
```
</details>

## ❖ Available Algorithms
PyPOTS supports imputation, classification, clustering, and forecasting tasks on multivariate time series with missing values. The currently available algorithms of four tasks are cataloged in the following table with four partitions. The paper references are all listed at the bottom of this readme file. Please refer to them if you want more details.

|   ***`Imputation`***   |      🚥      |                                                                                        🚥                                                                                         |    🚥    |
|:----------------------:|:------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|
|        **Type**        |  **Abbr.**   |                                                                    **Full name of the algorithm/model/paper**                                                                     | **Year** |        
|       Neural Net       |    SAITS     |                                                               Self-Attention-based Imputation for Time Series [^1]                                                                |   2023   |
|       Neural Net       | Transformer  | Attention is All you Need [^2];<br>Self-Attention-based Imputation for Time Series [^1];<br><sub>Note: proposed in [^2], and re-implemented as an imputation model in [^1].</sub> |   2017   |
|       Neural Net       |    BRITS     |                                                              Bidirectional Recurrent Imputation for Time Series [^3]                                                              |   2018   |
|         Naive          |     LOCF     |                                                                         Last Observation Carried Forward                                                                          |    -     |
| ***`Classification`*** |      🚥      |                                                                                        🚥                                                                                         |    🚥    |
|        **Type**        |  **Abbr.**   |                                                                    **Full name of the algorithm/model/paper**                                                                     | **Year** |
|       Neural Net       |    BRITS     |                                                              Bidirectional Recurrent Imputation for Time Series [^3]                                                              |   2018   |
|       Neural Net       |    GRU-D     |                                                  Recurrent Neural Networks for Multivariate Time Series with Missing Values [^4]                                                  |   2018   |
|       Neural Net       |   Raindrop   |                                                    Graph-Guided Network for Irregularly Sampled Multivariate Time Series [^5]                                                     |   2022   |
|   ***`Clustering`***   |      🚥      |                                                                                        🚥                                                                                         |    🚥    |
|        **Type**        |  **Abbr.**   |                                                                    **Full name of the algorithm/model/paper**                                                                     | **Year** |
|       Neural Net       |     CRLI     |                                                      Clustering Representation Learning on Incomplete time-series data [^6]                                                       |   2021   |
|       Neural Net       |    VaDER     |                                                                  Variational Deep Embedding with Recurrence [^7]                                                                  |   2019   |
|  ***`Forecasting`***   |      🚥      |                                                                                        🚥                                                                                         |    🚥    |
|        **Type**        |  **Abbr.**   |                                                                    **Full name of the algorithm/model/paper**                                                                     | **Year** |
|     Probabilistic      |     BTTF     |                                                                    Bayesian Temporal Tensor Factorization [^8]                                                                    |   2021   |


## ❖ Citing PyPOTS
We are pursuing to publish a short paper introducing PyPOTS in prestigious academic venues, e.g. JMLR (track for 
[Machine Learning Open Source Software](https://www.jmlr.org/mloss/)). Before that, PyPOTS is using its DOI from Zenodo 
for reference. If you use PyPOTS in your research, please cite it as below and 🌟star this repository to make others 
notice this work. 🤗

```bibtex
@misc{du2022PyPOTS,
author = {Wenjie Du},
title = {{PyPOTS: A Python Toolbox for Data Mining on Partially-Observed Time Series}},
year = {2022},
howpublished = {\url{https://github.com/wenjiedu/pypots}},
url = {\url{https://github.com/wenjiedu/pypots}},
doi = {10.5281/zenodo.6823221},
}
```

or

`Wenjie Du. (2022). PyPOTS: A Python Toolbox for Data Mining on Partially-Observed Time Series. Zenodo. 
https://doi.org/10.5281/zenodo.6823221`


## ❖ Contribution
You're very welcome to contribute to this exciting project! 

By committing your code, you'll
- be listed as one of [PyPOTS contributors](https://github.com/WenjieDu/PyPOTS/graphs/contributors): <a href="https://github.com/wenjiedu/pypots/graphs/contributors"><img align="center" src="https://contrib.rocks/image?repo=wenjiedu/pypots"></a>;
- get mentioned in our [release notes](https://github.com/WenjieDu/PyPOTS/releases);

Besides, you can also contribute to PyPOTS by simply staring🌟 this repo to help more people notice it. 
Your star is your recognition to PyPOTS, and it matters! 

<details>
<summary><b><i>👏 Click here to view PyPOTS stargazers and forkers.<br>We're so proud to have more and more awesome users, as well as more bright ✨stars: </i></b></summary>
<a href="https://github.com/WenjieDu/PyPOTS/stargazers"><img alt="PyPOTS stargazers" src="https://reporoster.com/stars/dark/WenjieDu/PyPOTS"></a>
<a href="https://github.com/WenjieDu/PyPOTS/network/members"><img alt="PyPOTS forkers" src="https://reporoster.com/forks/dark/WenjieDu/PyPOTS"></a>
</details>


## ❖ Attention 👀
The documentation and tutorials are under construction. 

‼️ PyPOTS is currently under developing. If you like it and look forward to its growth, <ins>please give PyPOTS a star 
and watch it to keep you posted on its progress and to let me know that its development is meaningful</ins>. If you have 
any feedback, or want to contribute ideas/suggestions or share time-series related algorithms/papers, please join PyPOTS 
community and chat on <a href="https://join.slack.com/t/pypots-dev/shared_invite/zt-1gq6ufwsi-p0OZdW~e9UW_IA4_f1OfxA"><img alt="Slack Workspace" align="center" src="https://img.shields.io/badge/Slack-join_us!-grey?logo=slack&color=teal"></a>, 
or create an issue. If you have any additional questions or have interests in collaboration, please take a look at 
[my GitHub profile](https://github.com/WenjieDu) and feel free to contact me 🤝.

Thank you all for your attention! 😃


[^1]: Du, W., Cote, D., & Liu, Y. (2023). [SAITS: Self-Attention-based Imputation for Time Series](https://doi.org/10.1016/j.eswa.2023.119619). *Expert systems with applications*.
[^2]: Vaswani, A., Shazeer, N.M., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, L., & Polosukhin, I. (2017). [Attention is All you Need](https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html). *NeurIPS 2017*.
[^3]: Cao, W., Wang, D., Li, J., Zhou, H., Li, L., & Li, Y. (2018). [BRITS: Bidirectional Recurrent Imputation for Time Series](https://papers.nips.cc/paper/2018/hash/734e6bfcd358e25ac1db0a4241b95651-Abstract.html). *NeurIPS 2018*.
[^4]: Che, Z., Purushotham, S., Cho, K., Sontag, D.A., & Liu, Y. (2018). [Recurrent Neural Networks for Multivariate Time Series with Missing Values](https://www.nature.com/articles/s41598-018-24271-9). *Scientific Reports*.
[^5]: Zhang, X., Zeman, M., Tsiligkaridis, T., & Zitnik, M. (2022). [Graph-Guided Network for Irregularly Sampled Multivariate Time Series](https://arxiv.org/abs/2110.05357). *ICLR 2022*.
[^6]: Ma, Q., Chen, C., Li, S., & Cottrell, G. W. (2021). [Learning Representations for Incomplete Time Series Clustering](https://ojs.aaai.org/index.php/AAAI/article/view/17070). *AAAI 2021*.
[^7]: Jong, J.D., Emon, M.A., Wu, P., Karki, R., Sood, M., Godard, P., Ahmad, A., Vrooman, H.A., Hofmann-Apitius, M., & Fröhlich, H. (2019). [Deep learning for clustering of multivariate clinical patient trajectories with missing values](https://academic.oup.com/gigascience/article/8/11/giz134/5626377). *GigaScience*.
[^8]: Chen, X., & Sun, L. (2021). [Bayesian Temporal Factorization for Multidimensional Time Series Prediction](https://arxiv.org/abs/1910.06366). *IEEE transactions on pattern analysis and machine intelligence*.

<details>
<summary>🏠 Visits</summary>
<a href="https://github.com/WenjieDu/PyPOTS">
    <img alt="PyPOTS visits" align="left" src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FPyPOTS%2FPyPOTS&count_bg=%23009A0A&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Hits&edge_flat=false">
</a>
</details>
