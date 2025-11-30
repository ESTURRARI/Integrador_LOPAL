import csv

# abre o CSV (mesma pasta do script)
with open("LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)  # ignora cabeçalho

    linhas = list(leitor)

# função que retorna emoji + texto curto 
def interpretar(valor):
    v = int(valor)
    if v == 0:
        return "🔴 (parada)"
    elif v == 1:
        return "🟡 (baixa)"
    else:
        return "🟢 (ok)"

# montando o HTML
html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Status das Esteiras - Monitoramento de Estoque</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    h1 { color: #000000; }
    table { border-collapse: collapse; width: 100%; max-width: 800px; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
    th { background: #f0f0f0; }
    .vermelho { background: #ffdede; }   
    .amarelo { background: #fff6d6; }    
    .verde { background: #e7ffe7; }     
  </style>
</head>
<body>
  <h1>Status das Esteiras - Monitoramento de Estoque</h1>
  <table>
    <tr>
      <th>Data</th><th>Hora</th><th>Esteira 1</th><th>Esteira 2</th><th>Esteira 3</th>
    </tr>
"""

for linha in linhas:
    data, hora, e1, e2, e3 = linha[0], linha[1], linha[2], linha[3], linha[4]
    # define classes para cor de fundo
    def cls(valor):
        return "vermelho" if int(valor)==0 else ("amarelo" if int(valor)==1 else "verde")
    html += f"<tr>\n"
    html += f"  <td>{data}</td><td>{hora}</td>\n"
    html += f"  <td class='{cls(e1)}'>{interpretar(e1)}</td>\n"
    html += f"  <td class='{cls(e2)}'>{interpretar(e2)}</td>\n"
    html += f"  <td class='{cls(e3)}'>{interpretar(e3)}</td>\n"
    html += f"</tr>\n"

html += """
  </table>
  <p style="margin-top:12px; font-size:0.9em; color:#333;">
    Legenda: 🔴 parada | 🟡 baixa | 🟢 normal
  </p>
</body>
</html>
"""

# salva o arquivo HTML
with open("Status_das_Esteiras.html", "w", encoding="utf-8") as out:
    out.write(html)

print("HTML gerado: Status_das_Esteiras.html")