import json
import pandas as pd
import os  # To create dirs if needed

# Create data/ if not exists
os.makedirs('data', exist_ok=True)

# Load your JSON
with open('summaries/paper_summaries.json', 'r') as f:
    data = json.load(f)

# Assign sub_theme function
def assign_sub_theme(title, key_contrib):
    text = (title.lower() + ' ' + key_contrib.lower())
    if any(word in text for word in ['threat', 'detection', 'anomaly', 'fraud', 'soc']):
        return 'Threat Detection'
    elif any(word in text for word in ['compliance', 'framework', 'regulation', 'act', 'standard', 'gdpr', 'nist']):
        return 'Compliance Frameworks'
    elif any(word in text for word in ['explainable', 'xai', 'bias', 'ethics', 'fairness', 'transparency']):
        return 'XAI & Ethics'
    elif any(word in text for word in ['agentic', 'autonomous', 'multi-agent']):
        return 'Agentic AI'
    elif any(word in text for word in ['generative', 'genai']):
        return 'Generative AI Risks'
    else:
        return 'General Auditing'

# Add sub_theme
for d in data:
    d['sub_theme'] = assign_sub_theme(d['title'], d['key_contrib'])

# Save updated JSON (optional)
with open('summaries/paper_summaries_updated.json', 'w') as f:
    json.dump(data, f, indent=2)

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