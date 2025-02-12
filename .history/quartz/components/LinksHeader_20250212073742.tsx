import { QuartzComponentConstructor } from "./types"
import style from "./styles/linksHeader.scss"

interface Options {
  links: Record<string, string>
}

export default (() => {
  function LinksHeader() {
    return null
  } //null

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor
