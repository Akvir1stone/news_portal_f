from django.db import models

# CREATE TABLE authors (
# 	author_id SERIAL PRIMARY KEY,
# 	auth_name TEXT NOT NULL,
# );

class Authors(models.Model):
    auth_name = models.CharField(max_length=300)

# CREATE TABLE articles (
# 	article_id SERIAL PRIMARY KEY,
# 	article_text TEXT NOT NULL,
# 	author_id INT REFERENCES authors(author_id),
# 	publ_date DATE NOT NULL,
# );


class Articles(models.Model):
    article_text = models.TextField
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publ_date = models.DateField()