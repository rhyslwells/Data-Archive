import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [Component.LinksHeader()],
  afterBody: [
    // Component.Breadcrumbs(),
    // Component.TagList(),
    Component.Backlinks(),
    Component.Comments({
      provider: 'giscus',
      options: {
        // from data-repo
        repo: 'rhyslwells/Data-Archive',
        // from data-repo-id
        repoId: 'R_kgDOMuMI-Q',
        // from data-category
        category: 'Announcements',
        // from data-category-id
        categoryId: 'DIC_kwDOMuMI-c4CjvGU',
      }
    }),
    Component.MobileOnly(Component.Explorer({
      folderClickBehavior: "link"    })),
  ],
  footer: Component.Footer({
    links: {
    GitHub: "https://github.com/rhyslwells/Data-Archive",
    Linkedin: "https://www.linkedin.com/in/rhyslwells/"  },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    // Component.Breadcrumbs(),
    // Component.Graph({
    //   localGraph: {
    //     drag: true, // whether to allow panning the view around
    //     zoom: true, // whether to allow zooming in and out
    //     depth: 1, // how many hops of notes to display
    //     scale: 0.8, // default view scale 
    //     repelForce: 0.5, // how much nodes should repel each other
    //     centerForce: 0.3, // how much force to use when trying to center the nodes
    //     linkDistance: 30, // how long should the links be by default?
    //     fontSize: 0.6, // what size should the node labels be?
    //     opacityScale: 1, // how quickly do we fade out the labels when zooming out?
    //     removeTags: [], // what tags to remove from the graph
    //     showTags: false, // whether to show tags in the graph
    //   },
    //   globalGraph: {
    //     drag: true,
    //     zoom: true,
    //     depth: -1,
    //     scale: 0.9,
    //     repelForce: 0.5,
    //     centerForce: 0.3,
    //     linkDistance: 30,
    //     fontSize: 0.6,
    //     opacityScale: 1,
    //     removeTags: [], // what tags to remove from the graph
    //     showTags: true, // whether to show tags in the graph
    //   },
    // }    ),
    Component.ArticleTitle(),
    // Component.ContentMeta(),
    Component.MobileOnly(Component.TableOfContents()),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer({
      folderClickBehavior: "link"
      // sortFn: sortFn,
    })),
  ],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    // Component.TagList(),
    // Component.Graph({
    //   localGraph: {
    //     drag: true, // whether to allow panning the view around
    //     zoom: true, // whether to allow zooming in and out
    //     depth: 1, // how many hops of notes to display
    //     scale: 1.1, // default view scale
    //     repelForce: 0.5, // how much nodes should repel each other
    //     centerForce: 0.3, // how much force to use when trying to center the nodes
    //     linkDistance: 30, // how long should the links be by default?
    //     fontSize: 0.6, // what size should the node labels be?
    //     opacityScale: 1, // how quickly do we fade out the labels when zooming out?
    //     removeTags: [], // what tags to remove from the graph
    //     showTags: false, // whether to show tags in the graph
    //   },
    //   globalGraph: {
    //     drag: true,
    //     zoom: true,
    //     depth: -1,
    //     scale: 0.9,
    //     repelForce: 0.5,
    //     centerForce: 0.3,
    //     linkDistance: 30,
    //     fontSize: 0.6,
    //     opacityScale: 1,
    //     removeTags: [], // what tags to remove from the graph
    //     showTags: true, // whether to show tags in the graph
    //   },
    // }    ),
    // Component.Graph(),
    //Component.DesktopOnly(Component.RecentNotes({
    //   title: "Recently Created",
    //   limit: 5
    // })),
    // Component.Backlinks(),
    // Component.TableOfContents(),
  ]
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer({
      folderClickBehavior: "link"})),
  ],
  right: [
    Component.MobileOnly(Component.Explorer({
      folderClickBehavior: "link"    })),
    // Component.DesktopOnly(Component.Graph()),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}
