import { createRouter, createWebHashHistory } from 'vue-router'
import Index from '@/views/Index'
import ProductDetail from '@/views/ProductDetail'
import FilterProducts from '@/views/FilterProducts'
import About from '@/views/About'
import Register from '@/views/Register'
import Blog from '@/views/Blog'
import BlogDetail from '@/views/BlogDetail'
import BrandsPage from '@/views/BrandsPage'
import Page404 from '@/views/404'
import CompareCart from '@/views/CompareCart'
import Profile from '@/views/Profile'
import MegaCategory from '@/views/MegaCategory'


const routes = [
  {
    path: '',
    name: 'index',
    component: Index
  },
  {
    path: '/detail/:product_id',
    name: 'productDetail',
    component: ProductDetail
  },
  {
    path: '/product_filters',
    name: 'productFilters',
    component: FilterProducts
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/blog',
    name: 'blog',
    component: Blog
  },
  {
    path: '/blog_detail/:id',
    name: 'blog_detail',
    component: BlogDetail
  },
  {
    path: '/brands',
    name: 'brands',
    component: BrandsPage
  },
  {
    path: '/404',
    name: '404',
    component: Page404
  },
  {
    path: '/compare_cart',
    name: 'compare',
    component: CompareCart
  },
  {
    path: '/profile/:id',
    name: 'profile',
    component: Profile
  },
  {
    path: '/mega_category/:id',
    name: 'mega_category',
    component: MegaCategory
  },
  
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
