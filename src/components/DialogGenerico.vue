<!-- DialogGenerico.vue -->
<template>
    <div v-if="mostrar" class="dialog-container">
        <h3>{{ titulo }}</h3>
        <form @submit.prevent="confirmar">
            <div v-for="(param, index) in parametros" :key="index">
                <label :for="param.nome">{{ param.nome }}</label>
                <input
                    v-if="param.tipo !== 'selecao'"
                    :type="param.tipo || 'number'"
                    :id="param.nome"
                    v-model="valores[param.nome]"
                />
                <select
                    v-else
                    :id="param.nome"
                    v-model="valores[param.nome]"
                >
                    <option value="horizontal">Horizontal</option>
                    <option value="vertical">Vertical</option>
                </select>
            </div>
            <button type="submit">Aplicar</button>
            <button type="button" @click="fechar">Cancelar</button>
        </form>
    </div>
</template>

<script>
import { ref } from 'vue';

export default {
    props: {
        titulo: String,
        parametros: Array, // [{ nome: 'dx', tipo: 'number' }, { nome: 'dy', tipo: 'number' }, ...]
        mostrar: Boolean
    },
    emits: ['confirmar', 'fechar'],
    setup(props, { emit }) {
        const valores = ref({});

        // Inicializa valores para os parâmetros
        props.parametros.forEach(param => {
            valores.value[param.nome] = param.tipo === 'selecao' ? 'horizontal' : 0;
        });

        const confirmar = () => {
            emit('confirmar', valores.value);
        };

        const fechar = () => {
            emit('fechar');
        };

        return { valores, confirmar, fechar };
    }
};
</script>

<style scoped>
/* Estilo do modal */
.dialog-container {
    /* Adicione seu estilo personalizado */
}
</style>
