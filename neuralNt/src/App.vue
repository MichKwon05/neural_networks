<template>
  <div>
    <h1>Convertidor de pulgadas a centímetros</h1>
    <input v-model="pulgada" type="number" placeholder="Ingrese la cantidad de pulgadas">
    <button @click="convertir">Convertir</button>
    <div v-if="resultado !== null">
      <p>{{ pulgada }} pulgadas son {{ resultado }} centímetros</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      pulgada: '',
      resultado: null
    };
  },
  methods: {
    async convertir() {
      try {
        const response = await axios.get('http://localhost:5000/convertir', {
          params: {
            pulgada: this.pulgada
          }
        });
        this.resultado = response.data.centimetros[0];
      } catch (error) {
        console.error('Error al convertir:', error);
      }
    }
  }
};
</script>
