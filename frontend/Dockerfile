FROM node:20-alpine

WORKDIR / app

# 1. Copie des descripteurs de paquets pour cacher l'étape npm install
COPY package*.json ./
RUN npm install

# 2. Copie du code source
COPY . .

# 3. Exposition du port Vite par défaut
EXPOSE 5173

# Le flag --host permet à Vite d'accepter les requêtes extérieures au conteneur
CMD ["npm", "run", "dev", "--", "--host"]
