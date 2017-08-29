# coding=UTF-8
from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013


class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0


        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_senteces_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)


# Main method, just run "python summary_tool.py"
def main():

    # Demo
    # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"

    content = """
    Gigster is shifting from letting anyone outsource full-stack app development to building next-gen tech projects for big companies. If an enterprise needs machine learning and vision, data visualization, blockchain, React or Swift work done and doesn’t want to hire full-time employees, Gigster assembles a squad of freelancers and guarantees the work at a fixed price.

With software eating everything, talent in high demand and tech rock stars seeking flexible schedules, Gigster is at the intersection of several massive trends. That’s why Redpoint is leading Gigster’s $20 million Series B joined by previous investor Andreessen Horowitz, and basketball legend Michael Jordan making one of his first tech investments. That brings the Gigster rocketship to $32.5 million in total funding just two years after launch.

“Since the invention of computers, new technologies have made programming languages exponentially higher level,” Gigster co-founder Roger Dickey tells me. “These shifts, combined with the ‘future of work’ accelerants such as freelancing and AI, have changed software engineering dramatically and will continue to do so.”



Freelance-fueled rocketship

When Gigster raised its 2016 Series A, it had just three enterprise clients. Since then it’s scaled up to more than 40, with project size up 10X and revenue up 3.5X to the double-digit millions per year. That’s because enterprises can afford to shell out the big bucks for high-quality development. When budgets are tight with small-to-medium sized businesses, “we’re able to do a good job for the client, but not always as good as the client wants. It’s a bit of a mismatch,” co-founder Roger Dickey explains. “With enterprises, our satisfaction has been off the charts.” Revenue is up 2.5X year-over-year.

Gigster works with more than 1,000 top-of-the-line freelancers sourced from Stanford, MIT, Facebook and Google. They can earn bonuses through the Gigster Fund that pays freelancers part of the returns if projects it invests in successfully exit.

Gigster claims to have 93 percent client satisfaction, with 94 percent of projects within budget and 96 percent of milestones hit on schedule. Clients include Pepsi, Wyndam Hotels and MasterCard, as well as eBay, Square and OpenTable. They could struggle to recruit, or let Gigster take care of it. The startup plans to triple in size by hiring 120 more employees with the new funding.



At its core, Gigster is fusing teams of freelancers with advanced project management tools and artificial intelligence to ensure gigs get done on time and on budget. That’s a rarity in the tech world, where the joke is that you should double any estimate you’re given about how long it will take to design and code something.

The frustration of finding gifted but reliable freelancers is what led Dickey to found Gigster. After building hit social game Dope Wars, selling it to Zynga where it was turned into Mafia Wars and working there a few years, he wanted to experiment with some new projects. He started Gigster with co-founder Debo Olaosebikan to make it easy for anyone to pay to get software designed, coded and delivered. It competes with traditional hiring and freelance marketplaces like Toptal, where clients have to manage projects themselves, with Gigster emphasizing its turn-key service.



From ‘build anyone an app’ to ‘enterprise code dirty work’

To fuel the enterprise pivot, Gigster raised the $20 million Series B from Redpoint, Andreessen and Jordan, as well as Y Combinator, Ashton Kutcher’s Sound Ventures, Marc Benioff and Quora CEO Adam D’Angelo. Dickey wouldn’t disclose the valuation but said “it was a substantial up round and we’re very pleased with the outcome.” Does Air Jordan bring any special skills to the cap table? Nope. “He was my childhood hero. It’s just fun to have him on the cap table,” Dickey laughs. “He didn’t put a ton into the round. We thought it’d be cool to have someone involved that we really look up to.”

Gigster already has luminary operators behind it, and chose Redpoint to lead the round because it’s a software-as-a-service expert. “We’re thinking of moving towards a SaaS model,” Dickey reveals. “It’s not going to happen immediately after the B round, but on top of selling [freelance development] services, we may sell some SaaS-based products as well.” He was cagey about what exactly those products would be, but they’d likely let enterprises use some of Gigster’s internal scoping and efficiency tools on their in-house projects.

“There’s a new model in consulting, combining freelance talent with automation tools. That’s the reason Gigster exists,” Dickey tells me. “I think now is the right time to start this company as there’s structured data on work. Companies are leaving data in Asana, Trello, Slack . . . they’re leaving digital footprints. Our platform sucks out that structured data.”



For example, Gigster has mapped out 1,000 past projects to build a calculator that automatically processes time and budget proposals for potential clients. Its “Supervisor” tool knows how code check-ins and communication between engineers and the project manager should ramp up as a deadline approaches. “If you don’t see those actions happening, there’s a 91 percent chance you’re going to miss the milestone date,” Dickey says, which lets Gigster know when to step in to nudge freelancers or make changes.

These tools and more like its Team Builder, PM Assistant and Code Librarian could be invaluable to companies working on lots of projects, and give Gigster a SaaS-subscription revenue stream where it doesn’t have to pay out a big chunk to its freelancer teams. With all its new cash, Gigster can pay to build more SaaS tools, buy sales people to hock them and its freelancing service and add more fulfillment staff to the 15-person team that ensures gigs get done within the guaranteed schedule and budget.

Not every company will be able to adapt to the software revolution on their own. And with advanced technologies like AI, blockchain and new mobile frameworks becoming more essential amidst a talent shortage, enterprises will need help. Gigster has a mercenary army at the ready.
    """

    # Create a SummaryTool object
    st = SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_senteces_ranks(content)

    # Build the summary with the sentences dictionary
    summary = st.get_summary(content, sentences_dic)

    # Print the summary
    print summary

    # Print the ratio between the summary length and the original length
    print ""
    print "Original Length %s" % (len(content))
    print "Summary Length %s" % len(summary)
    print "Summary Ratio: %s" % (100 - (100 * (len(summary) / len(content))))


if __name__ == '__main__':
    main()