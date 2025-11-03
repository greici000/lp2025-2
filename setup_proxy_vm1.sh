sudo bash -c 'cat > /etc/netplan/99-config-proxy.yaml' <<EOF
network:
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [192.168.10.10/24]
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4] 
  version: 2
EOF

# Aplica as novas configurações de rede
sudo netplan apply
echo "IP 192.168.10.10 configurado com sucesso."

echo "--- 2. INSTALANDO E CONFIGURANDO NGINX NA VM 1 (Proxy) ---"
sudo apt update -y
sudo apt install nginx -y

# Remove a config padrão
sudo rm -f /etc/nginx/sites-enabled/default 

# Configura o Reverse Proxy para encaminhar o tráfego para 192.168.10.20:8080
sudo bash -c 'cat > /etc/nginx/sites-available/reverse_proxy.conf' <<EOF
server {
    listen 80;
    server_name 192.168.10.10;

    location / {
        # DIRECIONAMENTO CRUCIAL: Aponta para a VM Backend na porta 8080
        proxy_pass http://192.168.10.20:8080; 
        
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF

# Habilita o site e reinicia o serviço
sudo ln -sf /etc/nginx/sites-available/reverse_proxy.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
echo "VM 1 (Reverse Proxy) configurada. PRONTO!"
