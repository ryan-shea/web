def render_new_bounty_roundup(to_email):
    from dashboard.models import Bounty
    from django.conf import settings
    subject = "Spooky Season Salutations"
    new_kudos_pks = [52, 1821, 2050]
    new_kudos_size_px = 150
    if settings.DEBUG and False:
        # for debugging email styles
        email_style = 2
    else:
        offset = 2
        email_style = (int(timezone.now().strftime("%V")) + offset) % 7

    kudos_friday = f'''
<h3>Happy Kudos Friday!</h3>
</p>
<p>
''' + "".join([f"<a href='https://gitcoin.co/kudos/{pk}/'><img style='max-width: {new_kudos_size_px}px; display: inline; padding-right: 10px; vertical-align:middle ' src='https://gitcoin.co/dynamic/kudos/{pk}/'></a>" for pk in new_kudos_pks]) + '''
</p>
    '''
    intro = f'''
<p>
Hey Gitcoiners,
</p>
<p>
    The jet lag from Devcon is slowly fading away — back at home, we've caught up from our absense and are buckling down for the next few months. With that said, it's time to kick off Web3 World, our newest virtual hackathon. It's a two-week virtual hang where Gitcoin community members and entrepreneurs from around the globe will work together and push blockchain to new frontiers. Ready to jump in? <a href="https://hackathons.gitcoin.co/web3-world/">Check the landing page for details to come.</a> The hackathon begins on October 28th and ends on the 11th.
</p>
<p>
    While our overlords were at Devcon, the product team might have asked you why you're participating in our hackathons. As we hone in on making the best virtual experience for all parties — hackers and sponsors alike — we're asking you for feedback. What problems do you see? How can we do better? What projects would you like to see as sponsors? Send your thoughts to <a href="mailto:frank@gitcoin.co">Frank</a> and we'll be endlessly grateful.
</p>
<p>
    Newsletter readers: the questions continue this week. We'd like to ask you about our humble publication. How do you like our new design? How can we improve our content? Do you like our jokes? <a href="https://consensys1mac.typeform.com/to/gz5aGK">Fill out this 30s survey. We'd love to hear your thoughts.</a>
</p>
{kudos_friday}
<h3>What else is new?</h3>
    <ul>
        <li>
        The Gitcoin Livestream is on for this week! Join us <a href="https://gitcoin.co/livestream"> at 2PM ET this Friday!</a>
        </li>
        <li>
        As the title of this email suggests, October is in full effect. You know what that means. Help contribute to open source and earn some rad prizes with Hacktoberfest — now is the perfect time to work on open source bounties and get rewards for making pull requests. The info? Who has it? <a href="https://hacktoberfest.digitalocean.com/">They do.</a>
        </li>
    </ul>
</p>
<p>
Back to shipping,
</p>
'''
    highlights = [{
        'who': 'rshtirmer',
        'who_link': True,
        'what': 'Request for update: granted. Tensorforce support from 0.4.4 to 0.5.2',
        'link': 'https://gitcoin.co/issue/notadamking/tensortrade/42/3555',
        'link_copy': 'View more',
    }, {
        'who': 'nionis',
        'who_link': True,
        'what': 'Who loves a good lottery? Nionis.',
        'link': 'https://gitcoin.co/issue/enigmampc/EnigmaBounties/3/3262',
        'link_copy': 'View more',
    }, {
        'who': 'acolytec3',
        'who_link': True,
        'what': 'Alcolytec with the seed phrase fixes',
        'link': 'https://gitcoin.co/issue/status-im/status-react/8938/3528',
        'link_copy': 'View more',
    }, ]

    sponsor = {
        'name': 'MythX',
        'title': 'Keep Ethereum Secure',
        'image_url': '',
        'link': 'http://bit.ly/mythx-gitcoin-weekly',
        'cta': 'Get Started Now',
        'body': [
           'Built by a team of security researchers and experts, MythX is the premier security analysis service for Ethereum smart contracts.',
           'Scan for security vulnerabilities right away, from tools such as Truffle and VS Code. Pro options available for complete peace of mind.'
        ]
    }
    
    bounties_spec = [{
        'url': 'https://github.com/mainnebula/SPACE_TASKS/issues/6',
        'primer': 'Python Scripting: SQL Edition',
    }, {
        'url': 'https://github.com/notadamking/tensortrade/issues/41',
        'primer': 'Manage Contest Across All Components. Make it so.',
    }, {
        'url': 'https://github.com/ETHSydney/meetup-token/issues/3',
        'primer': 'Are you familiar with zero knowledge tools? Present!',
}, ]
