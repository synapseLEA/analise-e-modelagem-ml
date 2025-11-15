
import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from codigo_fonte.funcoes_auxiliares.limpar_dataframe import dataframeLimpo
df = dataframeLimpo()
from  sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix , accuracy_score , classification_report
import time

#Dividindo as variaveis 
Colunay = 'diagnosed_diabetes'
Y = df[Colunay]
X = df.drop(columns=['ethnicity', 'education_level', Colunay ,  'diabetes_stage'], axis=1)
X_train , X_test , Y_train , Y_test = train_test_split(X, Y , test_size= 0.3 , random_state=42 , stratify= Y)
metodo_random = RandomForestClassifier( n_estimators= 100 , max_depth=5 , random_state=42)
print ("\nIniciando treinamento do modelo...")
time.sleep(2)
#treinando modelo 
metodo_random.fit(X_train , Y_train)
print("\nTreinamento finalizado...")
#Resultados
previsao = metodo_random.predict(X_test)
acuracia = accuracy_score(Y_test , previsao)
matriz = confusion_matrix(Y_test , previsao)
print ("-=" * 30 )
print ("Resultados")
print (f'\n Acuracia : {acuracia *100:.2f}')
print (f'\nMatriz confusão : {matriz}')
print (classification_report(Y_test , previsao))
print ("-=" *30)

