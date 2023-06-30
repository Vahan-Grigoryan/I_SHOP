export default {
    methods: {
        redirectTo(where){
            const user = JSON.parse(localStorage.getItem('current_user'))
            this.$store.commit('setProfileContent', where)
            this.$router.push(`/profile/${user['id']}`)
        }
    }
}