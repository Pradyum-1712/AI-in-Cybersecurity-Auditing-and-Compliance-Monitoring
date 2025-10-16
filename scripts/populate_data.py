import json
import pandas as pd
import os  # To create dirs if needed

# Create data/ if not exists
os.makedirs('data', exist_ok=True)

# Load the JSON with sub_themes already assigned
with open('summaries/paper_summaries.json', 'r') as f:
    data = json.load(f)

# Generate CSVs
df_meta = pd.DataFrame([{
    'ref_id': d['ref_id'],
    'title': d['title'],
    'authors': ', '.join(d['authors']) if isinstance(d['authors'], list) else d.get('authors', 'N/A'),
    'year': d['year'],
    'publisher': d['publisher'],
    'theme': d['theme'],
    'sub_theme': d['sub_theme'],
    'link': d['link'],
    'key_contrib': d['key_contrib']
} for d in data])
df_meta.to_csv('data/papers_metadata.csv', index=False)

df_cat = df_meta.groupby('sub_theme')['ref_id'].apply(list).reset_index(name='ref_ids')
df_cat['num_papers'] = df_cat['ref_ids'].apply(len)
df_cat.to_csv('data/categorization.csv', index=False)

df_timeline = df_meta['year'].value_counts().sort_index().reset_index()
df_timeline.columns = ['year', 'count']
df_timeline['percentage'] = (df_timeline['count'] / len(df_meta) * 100).round(1)
df_timeline.to_csv('data/timeline_analysis.csv', index=False)