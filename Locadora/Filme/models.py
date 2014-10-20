#coding:utf-8
from django.db import models


# Create your models here.
FILMES_OP = [
	('Terror','Terror'),
	('Acao','Ação'),
	('Comedia','Comédia'),
	('Erotico','Erótico'),
	('Romance','Romance'),
	('Animacao','Animação'),
	('Suspense','Suspense')
]


SEXO_OPCOES = [
	('M','Masculino'),
	('F','Feminino')
]
class Categoria(models.Model):
	NomeCategoria = models.CharField('Categoria',max_length=20,null=True)
	Preco = models.DecimalField('Preço', max_digits=10, decimal_places=2, null=True)
	def __unicode__(self):
		return self.NomeCategoria

class Filme(models.Model):
	Nome_Filme = models.CharField('Nome do Filme',max_length=100,null=True)
	Classificacao = models.CharField('Classificação',max_length=20,choices=FILMES_OP, null=True)
	Categoria = models.ForeignKey(Categoria,verbose_name="Categoria",null=True)
	

	
	def __unicode__(self):
		return self.Nome_Filme


class Pessoa(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=14,null=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
	Estado = models.CharField('UF', max_length=2,null=True)
	CEP = models.CharField('CEP', max_length=9,null=True)
	def __unicode__(self):
		return self.Nome

class Alugar(models.Model):
	Cliente = models.ForeignKey(Pessoa, verbose_name="Cliente",null=True)
	DataAluguel = models.DateField('Data de Locação',null=True)
	DataEntrega = models.DateField('Data de Entrega',null=True)
	def __unicode__(self):
		return str(self.Cliente)
class subAluguel(models.Model):
	Aluguel = models.ForeignKey(Alugar,null=True)
	Filme_Alugar = models.ForeignKey(Filme, verbose_name="Filme",null=True)
