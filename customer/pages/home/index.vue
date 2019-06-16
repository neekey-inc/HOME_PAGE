<template>
  <section>
    <h1>国内1000社以上の代行会社を検索・比較・予約ができるサイト！</h1>
    <h3><i class="el-icon-search"></i>カテゴリ一括検索 | <i class="el-icon-check"></i>簡単比較 | <i class="el-icon-thumb"></i>サイト内で予約完了</h3>
    <h1>代行一覧</h1>
    <a @click="$router.push({name:'category'})"><el-link type="primary">一覧へ</el-link></a>
    <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="Category"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Description"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="Price">
      </el-table-column>
    </el-table>
    <h1>news(特集、キャンペーン)</h1>
    <a @click="$router.push({name:'news'})"><el-link type="primary">一覧へ</el-link></a>
    <div class="block">
      <el-carousel trigger="click" height="300px">
        <el-carousel-item v-for="news in newses" :key="news.id">
          <a @click="$router.push({name:'news-id', params:{id:news.id}})">
            <img :src="news.image" class="card-img-top" >
          </a>
        </el-carousel-item>
      </el-carousel>
    </div>
    <h1>比較</h1>
    <h2>相場</h2>
    <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="Category"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Description"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="Price">
      </el-table-column>
    </el-table>
    <h2>評価</h2>
    <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="Category"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Description"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="Price">
        <div class="reviewbox">
          <h3>name,age,srvice</h3>
          description
          <el-rate v-model="value1"></el-rate>
        </div>
      </el-table-column>
    </el-table>
    <h1>記事</h1>
    <a @click="$router.push({name:'article'})"><el-link type="primary">一覧へ</el-link></a>
    <div class="block">
      <el-carousel trigger="click" height="300px">
        <el-carousel-item v-for="article in articles" :key="article.id">
          <a @click="$router.push({name:'article-id', params:{id:article.id}})">
            <img :src="article.image" class="card-img-top" >
          </a>
        </el-carousel-item>
      </el-carousel>
    </div>
  </section>
</template>

<script>
  export default{
    data() {
      return {
        articles: [],
        newses: [],
        tableData: [{
          date: '家事代行',
          name: 'あなたの代わりに家事を行います',
          address: '¥ 2500~5000'
        }, {
          date: '育児代行',
          name: 'あなたの代わりに家事を行います',
          address: '¥ 2500~5000'
        }, {
          date: '掃除代行',
          name: 'あなたの代わりに家事を行います',
          address: '¥ 2500~5000'
        }, {
          date: 'お墓参り代行',
          name: 'あなたの代わりに家事を行います',
          address: '¥ 2500~5000'
        }]
      }
    },
    mounted() {
      this.fetchData()
      this.newsData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('article/')
        this.articles = res
        console.log('aaaa')
      },
      async newsData() {
        let res = await this.$axios.$get('news/')
        this.newses = res
        console.log('aaaa')
      }
    }
  }
</script>

<style>
</style>
