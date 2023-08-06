def LogModel():
    return r"$h_{\Theta}(x) = \sigma(\Theta^Tx) = \frac{1}{1+\exp{(-\Theta^Tx)}}$"

def PerceptronDef():
    return r"""
$h_{\theta}(X) = \text{sign}(\theta^TX)$

$J(\theta) = \frac{1}{m} \sum_{i=1}^{m}(1-\delta(y^{(i)},h_{\theta}(x^{(i)}))) \\ \delta(x, y)=\begin{cases} 1 & \text{, } x=y \\ 0 & \text{, } x\neq y \end{cases}$
"""

def SVMDef():
    return r"""
$h_{\theta}(X) = \text{sign}(\theta^TX)$

$J(\theta) = \frac{1}{m}\sum_{i=1}^ml(y^{(i)}\theta^Tx^{(i)}) \\ l(x)=max(1,1-x) \ \text{(hinge-loss funkcija)}$ 
"""

def LogisticRegressionDef():
    return r"""
$h_{\Theta}(x) = \sigma(\Theta^Tx) = \frac{1}{1+\exp{(-\Theta^Tx)}}$


$J(\Theta) = \sum_{i=1}^m\log{}(1 + \exp(-y^{(i)}\Theta^Tx^{(i)}))$

$J(\Theta, \theta_0) = \frac{1}{m}\sum\limits_{i=1}^{m}\left[-y^{(i)}\log{(h_{\Theta, \theta_0}(x^{(i)}))}-(1-y^{(i)})\log{(1-h_{\Theta, \theta_0}(x^{(i)}))}\right] + \frac{\lambda}{2}||\Theta||^2$
"""

def LinearRegressionDef():
    return r"""
$h_{\Theta, \theta_0}(x) = \theta_0 + \theta_1 x_1 + \dots + \theta_n x_n$


$J(\Theta, \theta_0) = \frac{1}{2m}\sum\limits_{i=1}^m (h_{\Theta, \theta_0}(x^{(i)}) - y^{(i)})^2$


$J(\Theta) = \frac{1}{2m}\sum\limits_{i=1}^m (h_{\Theta, \theta_0}(x^{(i)}) - y^{(i)})^2 + \lambda\sum_{i=1}^{m}\theta^2_i$
"""

def PolinomialRegressionDef():
    return r"""
$h_{\theta}(x)=\theta_0 + \sum_{i=1}^{m}\theta_ix_i$

$\frac{1}{2m}\sum\limits_{i=1}^m (h_{\Theta}(x^{(i)}) - y^{(i)})^2$

$\frac{1}{2}\sum\limits_{i=1}^m (h_{\Theta}(x^{(i)}) - y^{(i)})^2 + \frac{\lambda}{2}\Theta^T\Theta$
"""

def SoftmaxDef():
    return r"""
$h_{\theta}(x)=\sigma(\theta^Tx) \\ \sigma(z)_j=\frac{e^{z_j}}{\sum_{l=1}^{k}e^{z_l}}$

$P(Y|X;\theta) = \prod_{i=1}^mP(y^{(i)}|x^{(i)}; \theta) \to \mathrm{max}_{\theta} \ \text{(Max-likelyhood funkcija)}$

$-\log{}P(Y|X;\theta) = -\sum_{i=1}^m\log{}P(y^{(i)}|x^{(i)}; \theta) \to \mathrm{min}_{\theta}$
"""