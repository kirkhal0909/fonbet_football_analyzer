<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="fonbet_football_analyzer_0"></a>fonbet_football_analyzer</h1>
<p class="has-line-data" data-line-start="1" data-line-end="2">Fonbet парсер матчей по футболу и анализ</p>
<p class="has-line-data" data-line-start="3" data-line-end="5"><strong>class</strong> <strong>FonbetDataDownloader</strong>(<strong>daysDownload</strong>=-1,** varDatetime**=None, <strong>rewriteMode</strong>=False,<br>
<strong>timeWaitNextRequest</strong>=5, <strong>autoRecconect</strong>=True, <strong>timeAutoRecconect</strong>=20)</p>
<p class="has-line-data" data-line-start="6" data-line-end="7"><strong>FonbetDataDownloader</strong> - класс для загрузки матчей по футболу</p>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="___8"></a>параметры инициализации класса</h3>
<p class="has-line-data" data-line-start="9" data-line-end="15"><strong>daysDownload</strong> - (integer) сколько загрузить дней. Если значение меньше 0, он остановится от ошибки когда столкнётся с другим форматом или если остановить скрипт самостоятельно.<br>
<strong>varDatetime</strong> - (datetime) дата с которой начинать загрузку. После продолжает загрузку в прошлых днях 02.06.2021 =&gt; 01.06.2021 =&gt; …<br>
<strong>rewriteMode</strong> - (boolean) перезаписывать файлы с матчами<br>
<strong>timeWaitNextRequst</strong> - (integer) Сколько ждать секунд перед следующим запросом<br>
<strong>autoRecconect</strong> - (boolean) отправлять снова запрос, если соединение не удалось<br>
<strong>timeAutoRecconect</strong> - (integer) количество секунд, через которое сделать повторный запрос если autoRecconect=True</p>
<h3 class="code-line" data-line-start=16 data-line-end=17 ><a id="__16"></a>методы класса</h3>
<p class="has-line-data" data-line-start="17" data-line-end="23"><strong>FonbetDataDownloader</strong>.<strong>setDatetime</strong>(varDatetime) - изменить дату загрузки<br>
<strong>FonbetDataDownloader</strong>.<strong>getDate</strong>() - получить дату загрузки<br>
<strong>FonbetDataDownloader</strong>.<strong>addDays</strong>(days=1) - изменить дату загрузки, добавить дней days=n<br>
<strong>FonbetDataDownloader</strong>.<strong>minusDays</strong>(days=1) - изменить дату загрузки, сделать дату на дней days=n меньше<br>
<strong>FonbetDataDownloader</strong>.<strong>getRequest</strong>() - получить последний запрос<br>
<strong>FonbetDataDownloader</strong>.<strong>download</strong>(daysDownload=0) - загрузить daysDownload=n дней. Если значение 0, то берётся значение при инициализации класса</p>
<ul>
<li class="has-line-data" data-line-start="24" data-line-end="25"></li>
</ul>
<p class="has-line-data" data-line-start="25" data-line-end="27"><strong>FootballDataAnalyzer</strong>() - класс для анализа на основе загруженных данных.<br>
При инициализации <strong>football</strong> = <strong>FootballDataAnalyzer</strong>() создаётся CSV файл</p>
