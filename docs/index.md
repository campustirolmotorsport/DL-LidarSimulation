# Simulation

Das Ziel dieser Simulation ist es Testdaten zu generieren um Algorithmen für das autonome Fahren zu testen und zu entwickeln. Hierbei ist das Ziel möglich Realitätsnah zuarbeiten. Dafür gilt es Schwankungen und Messungenauigkeiten zu integrieren. Um das Arbeiten zu vereinfachen wird versuch alle Schritte zusätzlich Grafisch zu rendern.

## Strecke

Im ersten Schritt soll eine Strecke erstellt werden. Eine Stecke ist eine Funktion, welche folgende Eigenschaften erfüllt:

- geschlossen
- stetig

### Form

Im ersten Anlauf war der Versuch eine 3 Dimensionale implizite Funktion zu verwenden. Somit folgte:

$$F =\{x, y, z\} \in \mathbb{R}^3 | z = f(x,y)$$

Somit folgt Strecke, welche durch die Schnittpunkt der Funktion $f$ und der $Z$-Ebene angeben ist. Bei diesem Ansatz ist es sehr aufwendig die daraus resultierende Fläche zu berechnen, weil jeder Punkt des Bereiches betrachtet werden muss. Zudem ist die Berechnung des Bogenlänge sehr mühsam.

Somit wird nun die Parameterform verwenden, somit wir die Track-Funktion  $t(d) = \begin{pmatrix}x(d)\\y(d)\end{pmatrix}$ erhalten. Diese ist von der Distanz $d$ vom Start definiert. Somit ist $d = 0$ automatisch als Start definiert. Außerdem limitieren wir zu begin den Raum auf $R^2$.

#### Beispiel

$$t(d) = \begin{pmatrix}
6*sin(d) \\
3*cos(d) \end{pmatrix}$$

## Hütchen

Bei einem Rennen ist die Strecke durch Hütchen begrenz, welche auf denen Seiten den Rand der Fahrbahn markieren. Die Hütchen sind Blau und Gelb, welches jeweils eine Seite markiert.

Die Hütchen sollten auf beiden Seiten gleich weit von der Fahrbahn entfernt sein. Diese Entfernung wird mit der Bogenlänge berechnet.

Hierbei wird die zur vor definierte Funktion $f$ in Parameterform verwendet:
$$f(t) = \begin{pmatrix} x(t)\\y(t)\end{pmatrix}$$

Diese wird für die Berechnung in ihr Richtungskomponenten unterteilt.

$$d = \int^{t_1}_{t_2}\sqrt{ \bigg( \frac{dx}{dt}x(t)\bigg)^2 + \bigg(\frac{dy}{dt}y(t)\bigg)^2}$$

Somit lässt sich die Entfernung $d$ zwischen zwei Punkten entlang der Funktion berechnen.

Somit kann iterativ mittels der Auflösung `field.scale` die Position der folgenden Hütchen berechnet werden.

Jetzt wird die Orthogonale $o(x)$ des Punktes $p$ zur Fahrbahn berechnet werden.

$$p=\begin{pmatrix}x_0\\ y_0\end{pmatrix}$$

Somit folgt die Orthogonale $o(x)$:

$$o(x) = \begin{pmatrix}x_0 \\ y_0 \end{pmatrix} + \begin{pmatrix}\frac{df}{dy}-y(x_o) \\ \frac{df}{dx}x(x_o) \end{pmatrix} * d$$

Jetzt können die Position der Hütchen mit

$$d^2 = x^2 + y^2$$

$$\begin{pmatrix}x_0 \\ y_0 \end{pmatrix} =  \begin{pmatrix} a & c\\b &d\end{pmatrix} * \lambda$$
$$\frac{x_0 - a}{c} = \frac{y_0 - b}{d}$$
