import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import About from "../views/About";
import Events from "../views/Events";
import EventDetail from "../views/EventDetail";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/events",
    name: "Events",
    component: Events,
  },
  {
    path: "/events/:id",
    component: EventDetail,
    propd: true,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
