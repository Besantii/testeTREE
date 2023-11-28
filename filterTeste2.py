import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Carregar os dados
# Substitua 'seu_dataframe.csv' pelo caminho do seu arquivo CSV contendo os dados
df = pd.read_csv('tiktok.csv')

# Definir stopwords
stopwords = ['fy', 'viral', 'fyp', 'parati', 'foryou', 'foryoupage', 'fypシ', 'capcut', 'foryourpage']

# Criar 6 nichos e suas hashtags associadas
nichos_hashtags = {
    'Moda': ['fashion', 'style', 'outfit', 'trend', 'clothes'],
    'Comédia': ['funny', 'lol', 'haha', 'humor', 'comedy'],
    'Viagem': ['travel', 'explore', 'adventure', 'wanderlust', 'destination'],
    'Música': ['music', 'song', 'singer', 'concert', 'playlist'],
    'Fitness': ['fitness', 'exercise', 'workout', 'health', 'active'],
    'Arte': ['art', 'painting', 'drawing', 'creative', 'artist']
}

# Adicionar uma coluna 'nicho' ao DataFrame
df['nicho'] = 'Outro'

# Pré-processamento das hashtags nas colunas 'body' e 'hashtags'
df['hashtags'] = df['hashtags'].apply(lambda x: ' '.join([word.lower() for word in str(x).split() if word.lower() not in stopwords]))
df['body'] = df['body'].apply(lambda x: ' '.join([word.lower() for word in str(x).split() if word.lower() not in stopwords]))

# Iterar sobre os nichos e atualizar a coluna 'nicho' se as hashtags coincidirem
for nicho, hashtags in nichos_hashtags.items():
    mask_hashtags = df['hashtags'].apply(lambda x: any(hashtag in x for hashtag in hashtags))
    mask_body = df['body'].apply(lambda x: any(hashtag in x for hashtag in hashtags))
    mask = mask_hashtags | mask_body
    df.loc[mask, 'nicho'] = nicho

# Dividir os dados em treino e teste
train_data, test_data, train_labels, test_labels = train_test_split(
    df['hashtags'], df['nicho'], test_size=0.2, random_state=42
)

# Criar um modelo de classificação
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# Treinar o modelo
model.fit(train_data, train_labels)

# Avaliar a precisão do modelo nos dados de teste
accuracy = model.score(test_data, test_labels)
print(f'Acurácia do modelo: {accuracy:.2f}')
