import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";

import About from "../views/About";
import ContactUs from "../views/ContactUs";
import FAQ from "../views/FAQ";
import Events from "../views/Events";
import EventDetail from "../views/EventDetail";
import NotFound from "../views/NotFound";

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
    path: "/faq",
    name: "FAQ",
    component: FAQ,
  },
  {
    path: "/contacts",
    name: "ContactUs",
    component: ContactUs,
  },
  {
    path: "/events",
    name: "Events",
    component: Events,
  },
  {
    path: "/events/:id",
    component: EventDetail,
    props: true,
  },
  { path: "/:notFound(.*)", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
