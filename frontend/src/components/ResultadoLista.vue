<template>
  <ul v-if="resultados.length">
    <li v-for="(item, index) in resultados" :key="index">
      {{ item.Nome_Fantasia }} - Registro: {{ item.Registro_ANS }} {{ item.CNPJ }}
    </li>
  </ul>
  <p v-else>Nenhum resultado encontrado.</p>
</template>

<script>
export default {
  props: {
    resultados: Array
  }
}
</script>
