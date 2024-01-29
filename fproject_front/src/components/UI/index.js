import MainTopSlider from '@/components/UI/MainTopSlider'
import MainBottomSlider from '@/components/UI/MainBottomSlider'
import MiniProductsSlider from '@/components/UI/MiniProductsSlider'
import Brands from '@/components/UI/Brands'
import HrefBlogBox from '@/components/UI/HrefBlogBox'
import BlogSlide from '@/components/UI/BlogSlide'
import Footer from '@/components/UI/Footer'
import BreadCrumbs from '@/components/UI/BreadCrumbs'
import MySelect from '@/components/UI/MySelect'
import OurProcs from '@/components/UI/OurProcs'
import ProfileContentEmpty from '@/components/UI/ProfileContentEmpty'
import Pagination from '@/components/UI/Pagination'
import SaleNewHit from '@/components/UI/DetectSaleNewHit'
import Slide from '@/components/UI/Slide'
import PaypalButtons from '@/components/UI/PayPalButtons'
import StripeButtons from '@/components/UI/StripeButtons'
import Modal from '@/components/UI/Modal'
import PaymentProcessLoading from '@/components/UI/PaymentProcessLoading'


export default [
    {...MainTopSlider, name: 'ui-main-top-slider'},
    {...MainBottomSlider, name: 'ui-main-bottom-slider'},
    {...MiniProductsSlider, name: 'mini-products-slider'},
    {...Brands, name: 'ui-brands'},
    {...HrefBlogBox, name: 'ui-href-blog-box'},
    {...BlogSlide, name: 'ui-blog-slide'},
    {...Footer, name: 'ui-footer'},
    {...BreadCrumbs, name: 'ui-bread-crumbs'},
    {...MySelect, name: 'ui-select'}, 
    {...OurProcs, name: 'ui-our-procs'},
    {...ProfileContentEmpty, name: 'ui-profile-empty'},
    {...Pagination, name: 'ui-pagination'},
    {...SaleNewHit, name: 'ui-detect-salenewhit'},
    {...Slide, name: 'ui-slide'},
    {...PaypalButtons, name: 'ui-paypal-btns'},
    {...StripeButtons, name: 'ui-stripe-btns'},
    {...Modal, name: 'ui-modal'},
    {...PaymentProcessLoading, name: 'ui-payment-process-loading'}
]
