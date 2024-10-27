<template>
    <div class="card">
        <Menubar :model="items">
            <template #start>
                <Image src="https://media.tenor.com/QUSMUwP4DX4AAAAi/plink-cat-blink.gif" width="40" />
            </template>
            <template #item="{ item, props, hasSubmenu, root }">
                <a v-ripple class="flex items-center" v-bind="props.action" @click="console.log(item.image)">
                    <!-- Condicional para exibir imagem ou ícone -->
                    <img
                        v-if="item.image"
                        :src="item.image"
                        class="icon-image"
                        alt="Item Image"
                        style="width: 30px; height: 30px;"
                    />
                    <span v-else :class="item.icon" />
                    <span class="ml-2">{{ item.label }}</span>
                    <Badge v-if="item.badge" :class="{ 'ml-auto': !root, 'ml-2': root }" :value="item.badge" />
                    <span v-if="item.shortcut"
                        class="ml-auto border border-surface rounded bg-emphasis text-muted-color text-xs p-1">{{
                            item.shortcut }}</span>
                    <i v-if="hasSubmenu"
                        :class="['pi pi-angle-down', { 'pi-angle-down ml-2': root, 'pi-angle-right ml-auto': !root }]"></i>
                </a>
            </template>
            <template #end>
                <div class="flex items-center gap-2">
                    <label for="integeronly" class="font-bold block mb-2">Bem-Vindo, Usuário Exemplo</label>
                    <Avatar image="https://media.tenor.com/Gz408T11T8gAAAAi/wiggle-cat-wiggle.gif" shape="circle" />
                </div>
            </template>
        </Menubar>
    </div>

    <!-- Modal -->
    <div v-if="imagemModal" class="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50" @click="fecharModal">
        <img :src="imagemModal" class="max-w-[80vw] max-h-[80vh] object-contain" @click.stop />
    </div>

    <!-- Modal de Translação -->
    <Dialog header="Transladar Imagem" v-model:visible="showTransladarModal" :modal="true" :closable="true">
        <div>
            <label for="dx">Deslocamento em X (dx):</label>
            <InputNumber v-model="translacao.dx" id="dx" />
        </div>
        <div class="mt-4">
            <label for="dy">Deslocamento em Y (dy):</label>
            <InputNumber v-model="translacao.dy" id="dy" />
        </div>
        <div class="mt-4 flex justify-end">
            <Button label="Aplicar" @click="aplicarTranslacao(translacao)" />
        </div>
    </Dialog>

    <!-- Modal de Rotação -->
    <Dialog header="Rotacionar Imagem" v-model:visible="showRotacionarModal" :modal="true" :closable="true">
        <div>
            <label for="angulo">Ângulo de Rotação:</label>
            <InputNumber v-model="rotacao.angulo" id="angulo" />
        </div>
        <div class="mt-4 flex justify-end">
            <Button label="Aplicar" @click="aplicarRotacao(rotacao.angulo)" />
        </div>
    </Dialog>

   <!-- Modal de Espelhamento -->
    <Dialog header="Espelhar Imagem" v-model:visible="showEspelharModal" :modal="true" :closable="true">
        <div>
            <label for="eixo">Eixo de Espelhamento: </label>
            <Select v-model="espelhamento" :options="eixos" optionLabel="name" placeholder="Selecione Eixo" class="w-full md:w-56" />
        </div>
        <div class="mt-4 flex justify-end">
            <Button label="Aplicar" @click="aplicarEspelhamento(espelhamento)" />
        </div>
    </Dialog>

    <!-- Modal de Aumento -->
    <Dialog header="Aumentar Imagem" v-model:visible="showAumentarModal" :modal="true" :closable="true">
        <div>
            <label for="fator-aumento">Fator de Aumento:</label>
            <InputNumber v-model="escala.fator" id="fator-aumento" />
        </div>
        <div class="mt-4 flex justify-end">
            <Button label="Aplicar" @click="aplicarAumento(escala.fator)" />
        </div>
    </Dialog>

    <!-- Modal de Diminuição -->
    <Dialog header="Diminuir Imagem" v-model:visible="showDiminuirModal" :modal="true" :closable="true">
        <div>
            <label for="fator-diminucao">Fator de Diminuição:</label>
            <InputNumber v-model="escala.fator" id="fator-diminucao" />
        </div>
        <div class="mt-4 flex justify-end">
            <Button label="Aplicar" @click="aplicarDiminuicao(escala.fator)" />
        </div>
    </Dialog>

    <div class="card">
        <div class="flex flex-col md:flex-row">
            <div class="w-full md:w-5/12 flex flex-col items-center justify-center gap-3 py-5">
                <FileUpload name="demo[]" url="/api/upload" :multiple="false"
                    accept="image/png, image/jpeg, image/jpg" :maxFileSize="1000000"
                    @select="onSelectedFiles">
                    <template #header="{ chooseCallback }">
                        <div class="flex flex-wrap justify-between items-center flex-1 gap-4">
                            <div class="flex gap-2">
                                <!-- Botão de upload visível somente se não houver imagem selecionada -->
                                <Button v-if="!imagemSelecionada" @click="chooseCallback()" icon="pi pi-images" rounded outlined
                                    severity="secondary"></Button>
                            </div>
                            <ProgressBar :value="totalSizePercent" :showValue="false"
                                class="md:w-20rem h-1 w-full md:ml-auto">
                                <span class="whitespace-nowrap">{{ totalSize }}B / 1Mb</span>
                            </ProgressBar>
                        </div>
                    </template>
                    <template #content="{ files, uploadedFiles, removeUploadedFileCallback, removeFileCallback }">
                        <div class="flex flex-col gap-8 pt-4">
                            <div v-if="files.length > 0">
                                <div class="flex flex-wrap gap-4">
                                    <div v-for="(file, index) of files" :key="file.name + file.type + file.size"
                                        class="p-8 rounded-border flex flex-col border border-surface items-center gap-4">
                                        <div>
                                            <img role="presentation" :alt="file.name" :src="file.objectURL" width="200"
                                                height="50" />
                                        </div>
                                        <span class="font-semibold text-ellipsis max-w-60 whitespace-nowrap overflow-hidden">
                                            {{ file.name }}
                                        </span>
                                        <div>{{ formatSize(file.size) }}</div>
                                        <Badge value="Aguardando Transformação" severity="warn" />
                                        <Button icon="pi pi-times"
                                            @click="onRemoveTemplatingFile(file, removeFileCallback, index)" outlined
                                            rounded severity="danger" />
                                    </div>
                                </div>
                            </div>

                            <div v-if="uploadedFiles.length > 0">
                                <h5>Completed</h5>
                                <div class="flex flex-wrap gap-4">
                                    <div v-for="(file, index) of uploadedFiles" :key="file.name + file.type + file.size"
                                        class="p-8 rounded-border flex flex-col border border-surface items-center gap-4">
                                        <div>
                                            <img role="presentation" :alt="file.name" :src="file.objectURL" width="200"
                                                height="50" />
                                        </div>
                                        <span class="font-semibold text-ellipsis max-w-60 whitespace-nowrap overflow-hidden">
                                            {{ file.name }}
                                        </span>
                                        <div>{{ formatSize(file.size) }}</div>
                                        <Badge value="Completed" class="mt-4" severity="success" />
                                        <Button icon="pi pi-times" @click="executarRemocaoEReset(index)" outlined
                                            rounded severity="danger" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                    <template #empty>
                        <div class="flex items-center justify-center flex-col">
                            <i class="pi pi-cloud-upload !border-2 !rounded-full !p-8 !text-4xl !text-muted-color" />
                            <p class="mt-6 mb-0">Arraste uma imagem até aqui para fazer upload</p>
                        </div>
                    </template>
                </FileUpload>

            </div>
            <div class="w-full md:w-2/12">
                <Divider layout="vertical" class="hidden md:flex"><b>PROCESSE SUA IMAGEM NO MENU</b></Divider>
            </div>
            <div class="w-full md:w-5/12 flex items-center justify-center py-5">
                <div v-if="imagemAtual" class="card">
                    <p class="mt-6 mb-0"><b>Imagem Processada</b></p>
                    <img :src="imagemAtual" alt="Imagem Processada" class="w-full" />
                    <div class="mt-4">
                        <Button label="Baixar Imagem" @click="baixarImagem" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { imagens, quantidadeImagens, itens, atualizarUltimasImagens } from './scripts/data.js';
import { 
    abrirImagem, 
    fecharModal, 
    formatSize, 
    onRemoveUploadedFile, 
    abrirTransladarModal,
    abrirRotacionarModal,
    abrirEspelharModal,
    abrirAumentarModal,
    abrirDiminuirModal,
    showTransladarModal,
    showRotacionarModal,
    showEspelharModal,
    showAumentarModal,
    showDiminuirModal,
    aplicarTranslacao as aplicarTranslacaoBackend,
    aplicarRotacao as aplicarRotacaoBackend,
    aplicarEspelhamento as aplicarEspelhamentoBackend,
    aplicarAumento as aplicarAumentoBackend,
    aplicarDiminuicao as aplicarDiminuicaoBackend,
    historicoImagens as affsCansei,
    imagemAtual
} from './scripts/functions.js';

import { items } from './scripts/menu.js';

const imagemSalva = sessionStorage.getItem('imagemProcessada');
if (imagemSalva) {
    imagemProcessada.value = imagemSalva;
}

const translacao = ref({ dx: 0, dy: 0 });
const rotacao = ref({angulo: 0}); // Número simples para rotação
const aumento = ref(1); // Número simples para aumento
const diminuicao = ref(1); // Número simples para diminuição
const selectedImage = ref(null);  // Variável para armazenar a imagem selecionada
const imagemProcessadaUrl = ref(null);  // Variável para armazenar a URL da imagem processada
const historicoImagens = ref([]); // Array para armazenar o histórico de imagens
const imagemSelecionada = ref(null);
const espelhamento = ref();
const eixos = ref([
    { name: 'Horizontal', code: 'horizontal' },
    { name: 'Vertical', code: 'vertical' }
]);
const escala = ref({fator: 0});

// Funções de ciclo de vida
onMounted(() => {
    atualizarUltimasImagens();
});
watchEffect(() => {
    atualizarUltimasImagens();
});

// Função para forçar o download da imagem
async function baixarImagem() {
    if (imagemProcessadaUrl.value) {
        try {
            const response = await fetch(imagemProcessadaUrl.value);
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'imagem-processada.jpg'; // Nome do arquivo a ser baixado
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            window.URL.revokeObjectURL(url);
        } catch (error) {
            console.error('Erro ao baixar a imagem:', error);
        }
    }
}

function executarRemocaoEReset(index) {
    removeUploadedFileCallback(index); // Chama a função de remoção
    imagemProcessadaUrl.value = null;  // Limpa a URL da imagem processada
    historicoImagens.value = []; // Opcional: limpa o histórico
}


// Função para aplicar a translação
async function aplicarTranslacao() {
    try {
        const url = await aplicarTranslacaoBackend(translacao.value, selectedImage.value || imagemProcessadaUrl.value);
        if (url) {
            imagemProcessadaUrl.value = url; // Atualiza a imagem processada atual
            historicoImagens.value.push(imagemProcessadaUrl.value); // Adiciona a imagem anterior ao histórico
            console.log("Imagens transladadas:", historicoImagens.value);
            console.log(affsCansei);

            translacao.value.dx = 0;
            translacao.value.dy = 0;
        } else {
            alert('Erro ao aplicar a translação.');
        }
    } catch (error) {
        console.error('Erro ao aplicar a translação:', error);
        alert('Erro ao aplicar a translação. Tente novamente.');
    }
}

function desfazerUltimaOperacao() {
    if (historicoImagens.value.length > 0) {
        imagemProcessadaUrl.value = historicoImagens.value.pop(); // Remove a última imagem do histórico
        alert('Última operação desfeita.');
    } else {
        alert('Não há operações para desfazer.');
    }
}



// Função para aplicar a rotação
async function aplicarRotacao() {
    const url = await aplicarRotacaoBackend(rotacao.value.angulo, selectedImage.value);
    if (url) {
        imagemProcessadaUrl.value = url;
        rotacao.value.angulo = 0;
    }
}

// Função para aplicar o espelhamento
async function aplicarEspelhamento() {
    const url = await aplicarEspelhamentoBackend(espelhamento.value.code, selectedImage.value);
    if (url) {
        imagemProcessadaUrl.value = url;
        espelhamento.value = 'horizontal'; // Resetando para valor padrão
    }
}

// Função para aplicar o aumento
async function aplicarAumento() {
    const url = await aplicarAumentoBackend(escala.value.fator, selectedImage.value);
    if (url) {
        imagemProcessadaUrl.value = url;
        escala.value.fator=0; // Resetando para valor padrão
    }
}

// Função para aplicar a diminuição
async function aplicarDiminuicao() {
    const url = await aplicarDiminuicaoBackend(escala.value.fator, selectedImage.value);
    if (url) {
        imagemProcessadaUrl.value = url;
        escala.value.fator=0; // Resetando para valor padrão
    }
}

// Função para lidar com arquivos selecionados
function onSelectedFiles(event) {
    const files = event.files; // arquivos selecionados
    if (files.length > 0) {
        selectedImage.value = files[0]; // Armazena o arquivo selecionado
        console.log('Imagem selecionada:', selectedImage.value);
    }
}

// Função para remover um arquivo da lista
function onRemoveTemplatingFile(file, removeFileCallback, index) {
    removeFileCallback(index);
    imagemProcessadaUrl.value = null;  // Limpa a URL da imagem processada
    historicoImagens.value = []; // Opcional: limpa o histórico
    // Verifica se a imagem removida era a selecionada
    if (imagemSelecionada.value && imagemSelecionada.value.name === file.name) {
        imagemSelecionada.value = null; // Limpa a imagem selecionada
    }
}

// Funções para abrir os modais
function openTransladarModal() {
    abrirTransladarModal();
}

function openRotacionarModal() {
    abrirRotacionarModal();
}

function openEspelharModal() {
    abrirEspelharModal();
}

function openAumentarModal() {
    abrirAumentarModal();
}

function openDiminuirModal() {
    abrirDiminuirModal();
}
</script>
