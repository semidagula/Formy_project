# To run a test in BDD

``` 
behave
```

""" cum vedem toate pachetele instalate """

behave --tags=smoke -f html -o raport.html

pt a rula un anumit feature:
behave .\features\checboxes.feature
