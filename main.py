import pandas as pd

# Configura o DDD
ddd = 69

# Carregue o arquivo CSV do Google Contacts
df = pd.read_csv("contacts.csv")

# Crie o DataFrame final com as colunas desejadas
df_final = pd.DataFrame({
    'id': range(1, len(df) + 1),
    'name': df['Name'],
    'email': '',
    'phone_number': df['Phone 1 - Value'].str.split(' ::: ').str[0]
})

# Remova espaços, "-" e parênteses da coluna phone_number
df_final['phone_number'] = df_final['phone_number'].str.replace(' ', '').str.replace('-', '').str.replace('(', '').str.replace(')', '')

# ------Correções de números------
# 021
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + x[3:] if str(x).startswith('021') else x)
# 0
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + x[1:] if str(x).startswith('0') else x)
# 98888888 > 8 > +55DDD9
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + str(ddd) + '9' + x if len(str(x)) == 8 else x)
# 998888888 > 9 > +55DDD
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + str(ddd) + x if len(str(x)) == 9 else x)
# DDD88888888 > 10 > +55
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + x if len(str(x)) == 10 else x)
# DDD998888888 > 11 > +55
df_final['phone_number'] = df_final['phone_number'].apply(lambda x: '+55' + x if len(str(x)) == 11 else x)

# Salve o DataFrame final em um novo arquivo CSV
df_final.to_csv("contacts_final.csv", index=False)

print("Finalizado")
