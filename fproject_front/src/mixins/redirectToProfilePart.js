export default {
    methods: {
        redirectTo(where){
            this.$store.commit('setProfileContent', where)
            this.$router.push('/profile/5')
        }
    }
}