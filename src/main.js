import "primeicons/primeicons.css"; // Ícones PrimeIcons
import "./style.css"; // Seu CSS personalizado
import "./flags.css"; // Outro CSS personalizado

import { createApp } from "vue";
import PrimeVue from "primevue/config";
import ConfirmationService from 'primevue/confirmationservice';
import DialogService from 'primevue/dialogservice';
import ToastService from 'primevue/toastservice';

import App from "./App.vue";
import AppState from './plugins/appState.js';
import ThemeSwitcher from './components/ThemeSwitcher.vue';
import Noir from './presets/Noir.js';

import Menubar from 'primevue/menubar'; // Importação direta do componente Menubar
import InputText from 'primevue/inputtext'; // Exemplo de importação de InputText
import InputNumber from 'primevue/inputnumber'; // Exemplo de importação de InputText
import Avatar from 'primevue/avatar'; // Exemplo de importação de Avatar
import Badge from 'primevue/badge'; // Exemplo de importação de Badge
import Ripple from 'primevue/ripple'; // Diretiva Ripple
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import FileUpload from 'primevue/fileupload';
import Button from 'primevue/button';
import ProgressBar from 'primevue/progressbar';
import Image from 'primevue/image';
import Divider from 'primevue/divider';
import Galleria from 'primevue/galleria';
import Dialog from 'primevue/dialog';
import Select from 'primevue/select';


// Importação de ícones
import { addIcons } from "oh-vue-icons";
import { CoResizeBoth } from "oh-vue-icons/icons";
addIcons(CoResizeBoth); // Adiciona o ícone ao projeto



const app = createApp(App);

app.use(PrimeVue, {
    theme: {
        preset: Noir,
        options: {
            prefix: 'p',
            darkModeSelector: '.p-dark',
            cssLayer: false,
        }
    }
});
app.use(AppState);
app.use(ConfirmationService);
app.use(ToastService);
app.use(DialogService);

app.component('Menubar', Menubar); // Registro do Menubar
app.component('InputText', InputText); // Registro de InputText
app.component('InputNumber', InputNumber); // Registro de InputNumber
app.component('Avatar', Avatar); // Registro de Avatar
app.component('Badge', Badge); // Registro de Badge
app.component('Splitter', Splitter); // Registro de Splitter
app.component('SplitterPanel', SplitterPanel); // Registro de Splitter Panel
app.component('FileUpload', FileUpload); // Registro de File Upload
app.component('Button', Button); // Registro de Button
app.component('ProgressBar', ProgressBar); // Registro de ProgressBar
app.component('Image', Image); // Registro de Image
app.component('Divider', Divider); // Registro de Divider
app.component('Galleria', Galleria); // Registro de Galleria
app.component('Dialog', Dialog); // Registro de Dialog
app.component('Select', Select); // Registro de Select
app.directive('ripple', Ripple); // Registro da diretiva Ripple

app.component('ThemeSwitcher', ThemeSwitcher);

app.mount("#app");
