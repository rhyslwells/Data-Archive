import { QuartzComponentConstructor } from "./types"
import style from "./styles/linksHeader.scss"

interface Options {
  links: Record<string, string>
}

export default (() => {
  function LinksHeader() {
    return (
      <div>
        <div id="links-header">
          <span>
            <a href="./pages/Data_Archive">Data Archive</a>
          </span>
          <span>
            <a href="./pages/Questions">Questions</a>
          </span>
          <span>
            <a href="./Monthly_Review/Goals">Goals</a>
          </span>
          <span>
            <a href="./Tasks">Tasks</a>
          </span>
        </div>
        <hr style={{ backgroundColor: 'var(--gray)', borderTop: '1px solid var(--gray)', marginTop: '1.3rem' }} />
      </div>
    )
  }

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor