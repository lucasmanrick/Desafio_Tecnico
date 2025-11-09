# CryptoTracker - Portfólio de Criptomoedas
Sistema fullstack de rastreamento de criptomoedas com app mobile Android (React Native) e AP##  Quick Start
### Backend (Django)
\`\`\`bash
cd backend
cp .env.example .env
docker-compose up --build
\`\`\`
 API: http://localhost:8000
 API Docs: http://localhost:8000/api/docs/
 Admin: http://localhost:8000/admin/ (user: admin, pass: admin123)
### Mobile (React Native)
\`\`\`bash
cd mobile
npm install
cp .env.example .env
# Edite .env e coloque:
# API_URL=http://10.0.2.2:8000 # Para emulador Android
# ou
# API_URL=http://SEU_IP_LOCAL:8000 # Para device físico
npm run android
\`\`\`
 App rodando no emulador/device
##  Stack Tecnológico
**Backend:**
- Django 5.0 + DRF
- PostgreSQL
- Redis + Celery
- Docker Compose
21
- JWT Authentication
**Mobile:**
- React Native 0.73
- TypeScript
- React Navigation
- TanStack Query
- Zustand
- Victory Native
**APIs:**
- CoinGecko API (preços de criptomoedas)
##  Funcionalidades
**Backend:**
- [x] Autenticação JWT completa
- [x] API REST documentada (Swagger)
- [x] Cache inteligente de preços (Redis)
- [x] Atualização automática de preços (Celery Beat)
- [x] Sistema de alertas de preço
- [x] Sincronização de portfólios
- [x] Health check completo
- [x] Docker Compose funcional
**Mobile:**
- [x] Autenticação (login/register)
- [x] Lista de criptomoedas com preços ao vivo
- [x] Detalhes com gráfico de histórico
- [x] Sistema de favoritos sincronizado
- [x] Portfólio com cálculo de lucro/perda
- [x] Alertas de preço
- [x] Dark mode
- [x] Pull-to-refresh
- [ ] Push notifications (não implementado)
- [ ] Biometria (não implementado)
##  Testes
**Backend:**
\`\`\`bash
cd backend
docker-compose run backend pytest
\`\`\`
**Mobile:**
22
\`\`\`bash
cd mobile
npm test
\`\`\`
##  Documentação
- [Documentação da API](./docs/API.md)
- [Arquitetura do Sistema](./docs/ARCHITECTURE.md)
##  Decisões Técnicas
### Por que Django + React Native?
Django oferece ORM robusto e ecosystem maduro. React Native permite desenvolver para Android e# Por que Celery?
Atualização de preços e verificação de alertas devem ser processadas em background sem bloquea# Por que Redis?
Cache de preços reduz drasticamente chamadas à CoinGecko API (rate limit). Também serve como b# Desafios Enfrentados
1. **Rate limiting da CoinGecko**: Implementei cache agressivo e Celery Beat para atualizar d **Sincronização mobile-backend**: React Query com cache + invalidação automática resolveu
 **Cálculo de lucro/perda**: Serializers do DRF calculam dinamicamente baseado em preços atu  Segurança
- Passwords hasheados com Django defaults
- JWT tokens com expiração
- CORS configurado
- Validação de inputs com serializers
- HTTPS em produção (recomendado)
##  Build Android
\`\`\`bash
cd mobile/android
./gradlew assembleRelease
# APK: android/app/build/outputs/apk/release/app-release.apk
\`\`\`
##  Autor
23
Lucas Manrick Teodoro da Fonseca - [lucasmanrick.ipms@gmail.com]