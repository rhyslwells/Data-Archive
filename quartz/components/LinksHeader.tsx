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
            <a href="/Data-Archive/pages/Data_Archive">Data Archive</a>
          </span>
          <span>
            <a href="/Data-Archive/0_Inbox/Questions">Questions</a>
          </span>
          <span>
            <a href="/Data-Archive/0_Inbox/Overview">Overview</a>
          </span>
          <span>
            <a href="/Data-Archive/0_Inbox/Tasks">Tasks</a>
          </span>
        </div>
        <hr style={{ backgroundColor: 'var(--gray)', borderTop: '1px solid var(--gray)', marginTop: '1.3rem' }} />
      </div>
    )
  }

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor
