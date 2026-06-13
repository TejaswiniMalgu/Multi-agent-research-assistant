from agents import build_reader_agent,build_search_agent,writer_chain,critic_chain


def run_research_pipeline(topic: str) -> dict:

    state = {}

    print("\n" + "=" * 50)
    print("Step-1..Search agent")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
    "messages": [
        (
            "user",
            f"""
            Search for information about: {topic}

            IMPORTANT:
            Return every source in this format:

            Title:
            URL:
            Snippet:

            Do not summarize.
            Do not omit URLs.
            """
                    )
                ]
        })

    state["search_result"] = str(
        search_result["messages"][-1].content
    )

    print("\nSearch Result\n", state["search_result"])

    print("\n" + "=" * 50)
    print("Step-2..Reader agent")

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""Based on the following search results about '{topic}',
pick the most relevant URL and scrape it for deeper content.

Search Results:
{state['search_result'][:800]}
"""
            )
        ]
    })

    state["scraped_content"] = str(
        reader_result["messages"][-1].content
    )

    print("\nScraped content\n", state["scraped_content"])

    print("\n" + "=" * 50)
    print("Step-3..Writer drafting")

    research_combined = (
    f"Search results:\n{state['search_result'][:2000]}\n\n"
    f"Detailed scraped content:\n{state['scraped_content'][:3000]}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFinal Report:\n", state["report"])

    print("\n" + "=" * 50)
    print("Step-4..Critic review")

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCritic report:\n", state["feedback"])

    return state

if __name__=="__main__":
    topic=input("\n Enter research topic\n")
    run_research_pipeline(topic)




