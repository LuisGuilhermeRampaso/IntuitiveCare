<template>
  <div class="app min-h-screen bg-gray-50">
    <header class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold text-gray-900">Busca de Operadoras de Saúde</h1>
      </div>
    </header>

    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <div class="px-4 py-6 sm:px-0">
        <div class="bg-white rounded-lg shadow-md p-6">
          <div class="flex flex-col sm:flex-row gap-4">
            <input
              v-model="termoBusca"
              @keyup.enter="buscar"
              placeholder="Digite nome, CNPJ ou registro ANS..."
              class="flex-grow p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            />
            
            <button
              @click="buscar"
              :disabled="!termoBusca.trim() || carregando"
              class="px-6 py-3 bg-blue-600 text-white font-medium rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              <span v-if="!carregando">Buscar</span>
              <span v-else class="flex items-center">
                <svg class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Buscando...
              </span>
            </button>
          </div>
        </div>

        <div v-if="erro" class="mt-4 bg-red-50 border-l-4 border-red-400 p-4">
          <div class="flex">
            <div class="flex-shrink-0">
              <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
              </svg>
            </div>
            <div class="ml-3">
              <p class="text-sm text-red-700">{{ erro }}</p>
            </div>
          </div>
        </div>

        <div v-if="resultados.length > 0" class="mt-6">
          <div class="bg-white shadow overflow-hidden sm:rounded-lg">
            <div class="px-4 py-5 sm:px-6 border-b border-gray-200">
              <h3 class="text-lg leading-6 font-medium text-gray-900">
                Resultados da busca
              </h3>
              <p class="mt-1 text-sm text-gray-500">
                Exibindo {{ resultados.length }} operadoras encontradas
              </p>
            </div>
            <ResultadoLista :resultados="resultados" />
          </div>
        </div>

        <div v-else-if="termoBusca && !carregando && !erro" class="mt-6 bg-white shadow overflow-hidden sm:rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <p class="text-center text-gray-500">Nenhuma operadora encontrada para "{{ termoBusca }}"</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import ResultadoLista from './components/ResultadoLista.vue';

export default {
  components: { ResultadoLista },
  data() {
    return {
      termoBusca: '',
      resultados: [],
      carregando: false,
      erro: null
    };
  },
  methods: {
    async buscar() {
      if (!this.termoBusca.trim()) return;
      
      this.carregando = true;
      this.erro = null;
      
      try {
        const res = await fetch(`http://localhost:5000/buscar?q=${encodeURIComponent(this.termoBusca)}`);
        
        if (!res.ok) {
          throw new Error(`Erro na requisição: ${res.status}`);
        }
        
        const data = await res.json();
        
        if (data.erro) {
          throw new Error(data.erro);
        }
        
        this.resultados = Array.isArray(data) ? data : data.dados || [];
      } catch (error) {
        console.error('Erro ao buscar:', error);
        this.erro = error.message || 'Ocorreu um erro ao buscar as operadoras';
        this.resultados = [];
      } finally {
        this.carregando = false;
      }
    }
  }
};
</script>