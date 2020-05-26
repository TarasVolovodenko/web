import Vue from 'vue'
import VueRouter from 'vue-router'
import issue from '../pages/issue.vue'
import event from '../pages/event.vue'
import issuesMap from '../pages/issues_map.vue'
import Homepage from '../pages/Homepage.vue'
import Contactspage from '../pages/Contactspage.vue'
import Donatepage from '../pages/Donatepage.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/issue',
        name: 'issue',
        component: issue
    },
    {
        path: '/event',
        name: 'event',
        component: event
    },
    {
        path: '/routerLink',
        name: 'routerLink',
        component: () =>
            import ('../layout/routerLink.vue')
    },
    {
        path: '/issuesMap',
        name: 'issuesMap',
        component: issuesMap
    },
    {
      path: '/',
      name: 'Homepage',
      component: Homepage
    },
    {
      path: '/contacts',
      name: 'Contacts',
      component: Contactspage
    },
    {
      path: '/donate',
      name: 'Donate',
      component: Donatepage
    }
]

const router = new VueRouter({
    routes
})

export default router
