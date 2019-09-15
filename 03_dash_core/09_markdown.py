import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown="""
Nagłówki

# H1
## H2
### H3
#### H4
##### H5
###### H6

Znaczniki tekstu:

Kursywa: *tekst kursywą* lub _tekst kursywa_  
Pogrubienie: **Tekst pogrubiony** lub __tekst pogrubiony__  
Kursywa i pogrubienie: **pogrubienie i _kursywa_**  
Przekreślenie: ~~Przekreślenie~~

Listy:

Lista uporządkowana:  
1. Python  
2. SQL  
3. Java  

Lista nieuporządkowana:
* Python
* SQL
* Java

Linkowanie 
[Google.com](http://www.google.com)

Kod

Użyj `print('Hello World')`

Blok kodu

```
import numpy as np

x = np.random.randn(100)
print(x)
```

```
SELECT * FROM products;
```

Table:

|UserID   |Rating    |Age|
|---------|----------|---|
|001      |4.5       |23 |
|002      |5         |34 |

Cytowanie:

> Python jest bardzo poręczny i łatwy do nauki.

Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. 
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. 
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty 
Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do 
realizacji druków na komputerach osobistych, jak Aldus PageMaker

> Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. 
Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. 
Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. 
Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty 
Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do 
realizacji druków na komputerach osobistych, jak Aldus PageMaker

Linie horyzontalne

---

***


"""


app.layout = html.Div([

    dcc.Markdown(markdown)
])

if __name__ == '__main__':
    app.run_server(debug=True)