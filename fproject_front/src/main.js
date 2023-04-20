import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import logic_components from '@/components/index'
import ui_components from '@/components/UI/index'
import VueSplide from '@splidejs/vue-splide';


App = createApp(App)

const components = [...logic_components, ...ui_components]
components.forEach( component => {
    App.component(component.name, component)
})

App
    .use(VueSplide)
    .use(store)
    .use(router)
    .mount('#app')
