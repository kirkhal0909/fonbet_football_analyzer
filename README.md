﻿﻿<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="fonbet_football_analyzer_0"></a>fonbet_football_analyzer</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">Fonbet парсер матчей по футболу и анализ</p>
<p class="has-line-data" data-line-start="3" data-line-end="9">По данным с Fonbet с 30.05.2020 по 01.06.2021 (136,537 матчей с погрешностью до [-1%:-2%] из-за проблем с одинаковым форматированием данных на сайте)<br>
шансы у команды которая забила 1-й гол:<br>
•70.55% выиграть<br>
•87.64% выиграть или выйти в ничью<br>
•12.36% проиграть<br>
В случае позднего первого гола следующая статистика (https://github.com/kirkhal0909/fonbet_football_analyzer/blob/main/stats/firstGoal.csv)</p>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Побед</th>
<th>Победа или ничья</th>
<th>Игр</th>
<th>Побед %</th>
<th>Победа или ничья %</th>
<th>Поражение %</th>
<th>с минуты</th>
</tr>
</thead>
<tbody>
<tr>
<td>63732</td>
<td>79349</td>
<td>88898</td>
<td>71.69%</td>
<td>89.26%</td>
<td>10.74%</td>
<td>10</td>
</tr>
<tr>
<td>47021</td>
<td>58364</td>
<td>64253</td>
<td>73.18%</td>
<td>90.83%</td>
<td>9.17%</td>
<td>20</td>
</tr>
<tr>
<td>34996</td>
<td>43334</td>
<td>46937</td>
<td>74.56%</td>
<td>92.32%</td>
<td>7.68%</td>
<td>30</td>
</tr>
<tr>
<td>26041</td>
<td>31914</td>
<td>34060</td>
<td>76.46%</td>
<td>93.70%</td>
<td>6.30%</td>
<td>40</td>
</tr>
<tr>
<td>17979</td>
<td>21646</td>
<td>22708</td>
<td>79.17%</td>
<td>95.32%</td>
<td>4.68%</td>
<td>50</td>
</tr>
<tr>
<td>12071</td>
<td>14212</td>
<td>14672</td>
<td>82.27%</td>
<td>96.86%</td>
<td>3.14%</td>
<td>60</td>
</tr>
<tr>
<td>7757</td>
<td>8834</td>
<td>9012</td>
<td>86.07%</td>
<td>98.02%</td>
<td>1.98%</td>
<td>70</td>
</tr>
<tr>
<td>4361</td>
<td>4786</td>
<td>4847</td>
<td>89.97%</td>
<td>98.74%</td>
<td>1.26%</td>
<td>80</td>
</tr>
</tbody>
</table>
<hr>
<p align="center">Тотал голов(всего голов за игру). Процент что забьют меньше или больше голов</p>
<table class="table table-striped table-bordered" align="center">
<thead>
<tr>
<th>Тотал голов</th>
<th>&lt;</th>
<th>&gt;</th>
</tr>
</thead>
<tbody>
<tr>
<td>0.5</td>
<td>7.28%</td>
<td>92.72%</td>
</tr>
<tr>
<td>1.5</td>
<td>23.53%</td>
<td>76.47%</td>
</tr>
<tr>
<td>2.5</td>
<td>44.1%</td>
<td>55.9%</td>
</tr>
<tr>
<td>3.5</td>
<td>63.77%</td>
<td>36.23%</td>
</tr>
<tr>
<td>4.5</td>
<td>78.03%</td>
<td>21.97%</td>
</tr>
<tr>
<td>5.5</td>
<td>87.39%</td>
<td>12.61%</td>
</tr>
<tr>
<td>6.5</td>
<td>92.88%</td>
<td>7.12%</td>
</tr>
<tr>
<td>7.5</td>
<td>96.05%</td>
<td>3.95%</td>
</tr>
<tr>
<td>8.5</td>
<td>97.87%</td>
<td>2.13%</td>
</tr>
<tr>
<td>9.5</td>
<td>98.85%</td>
<td>1.15%</td>
</tr>
</tbody>
</table>

<p align="center">Тотал голов если был забит первый гол с 10, 20, ... минуты</p>

|С 10 мин.|<|>||С 20 мин.|<|>||С 30 мин.|<|>||С 40 мин.|<|>||С 50 мин.|<|>||С 60 мин.|<|>||С 70 мин.|<|>||С 80 мин.|<|>|
|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|
|1.5|20.77%|79.23%||1.5|25.97%|74.03%||1.5|31.59%|68.41%||1.5|38.04%|61.96%||1.5|46.86%|53.14%||1.5|56.82%|43.18%||1.5|68.04%|31.96%||1.5|78.57%|21.43%|
|2.5|45.86%|54.14%||2.5|53.87%|46.13%||2.5|61.78%|38.22%||2.5|69.47%|30.53%||2.5|78.19%|21.81%||2.5|85.76%|14.24%||2.5|91.93%|8.07%||2.5|95.85%|4.15%|
|3.5|68.02%|31.98%||3.5|75.72%|24.28%||3.5|82.12%|17.88%||3.5|87.61%|12.39%||3.5|92.7%|7.3%||3.5|96.04%|3.96%||3.5|97.79%|2.21%||3.5|98.68%|1.32%|
|4.5|82.71%|17.29%||4.5|88.38%|11.62%||4.5|92.51%|7.49%||4.5|95.48%|4.52%||4.5|97.78%|2.22%||4.5|98.89%|1.11%||4.5|99.34%|0.66%||4.5|99.42%|0.58%|
|5.5|91.36%|8.64%||5.5|94.98%|5.02%||5.5|97.24%|2.76%||5.5|98.5%|1.5%||5.5|99.39%|0.61%||5.5|99.68%|0.32%||5.5|99.72%|0.28%||5.5|99.69%|0.31%|


<hr>
<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="fonbet_football_analyzer_0"></a>Script</h1>
<p class="has-line-data" data-line-start="21" data-line-end="23"><strong>class</strong> <strong>FonbetDataDownloader</strong>(<strong>daysDownload</strong>=-1,<strong>varDatetime</strong>=None, <strong>rewriteMode</strong>=False,<br>
<strong>timeWaitNextRequest</strong>=5, <strong>autoRecconect</strong>=True, <strong>timeAutoRecconect</strong>=20)</p>
<p class="has-line-data" data-line-start="24" data-line-end="25"><strong>FonbetDataDownloader</strong> - класс для загрузки матчей по футболу</p>
<h3 class="code-line" data-line-start=26 data-line-end=27 ><a id="___26"></a>параметры инициализации класса</h3>
<p class="has-line-data" data-line-start="27" data-line-end="33"><strong>daysDownload</strong> - (integer) сколько загрузить дней. Если значение меньше 0, он остановится от ошибки когда столкнётся с другим форматом или если остановить скрипт самостоятельно.<br>
<strong>varDatetime</strong> - (datetime) дата с которой начинать загрузку. После продолжает загрузку в прошлых днях 02.06.2021 =&gt; 01.06.2021 =&gt; …<br>
<strong>rewriteMode</strong> - (boolean) перезаписывать файлы с матчами<br>
<strong>timeWaitNextRequst</strong> - (integer) Сколько ждать секунд перед следующим запросом<br>
<strong>autoRecconect</strong> - (boolean) отправлять снова запрос, если соединение не удалось<br>
<strong>timeAutoRecconect</strong> - (integer) количество секунд, через которое сделать повторный запрос если autoRecconect=True</p>
<h3 class="code-line" data-line-start=34 data-line-end=35 ><a id="__34"></a>методы класса</h3>
<p class="has-line-data" data-line-start="35" data-line-end="41"><strong>FonbetDataDownloader</strong>.<strong>setDatetime</strong>(varDatetime) - изменить дату загрузки<br>
<strong>FonbetDataDownloader</strong>.<strong>getDate</strong>() - получить дату загрузки<br>
<strong>FonbetDataDownloader</strong>.<strong>addDays</strong>(days=1) - изменить дату загрузки, добавить дней days=n<br>
<strong>FonbetDataDownloader</strong>.<strong>minusDays</strong>(days=1) - изменить дату загрузки, сделать дату на дней days=n меньше<br>
<strong>FonbetDataDownloader</strong>.<strong>getRequest</strong>() - получить последний запрос<br>
<strong>FonbetDataDownloader</strong>.<strong>download</strong>(daysDownload=0) - загрузить daysDownload=n дней. Если значение 0, то берётся значение при инициализации класса</p>
<ul>
<li class="has-line-data" data-line-start="42" data-line-end="43"></li>
</ul>
<p class="has-line-data" data-line-start="43" data-line-end="45"><strong>FootballDataAnalyzer</strong>() - класс для анализа на основе загруженных данных.<br>
При инициализации <strong>football</strong> = <strong>FootballDataAnalyzer</strong>() создаётся CSV файл</p>