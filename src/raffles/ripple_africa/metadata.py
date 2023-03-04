import toolkit

POLICY_ID = "3568e07d31ab3c217ea594bfff9744a00a91225fa53244514ffeefb5"

NORMAL_IPFS = "QmdmRRGCmpWDuVvWfXaheba4FVEdR76AxeV1efs9nsNLha"
NORMAL_SUPPLY = 2475

GOLDENS = {
    "A Christmas Carol  #0446": {
        "ipfs": "QmXtxgZ7nQtU2LLo3T7ZMhaMsuRcGWe5BsaQ6WmKuQ4L7h",
    },
    "Antony and Cleopatra #1457": {
        "ipfs": "QmVeM85VbZUbdJdNAPYDnfUnxgtmej6SrgWUMHPcpZB5oG",
    },
    "A Tale of Two Cities #2326": {
        "ipfs": "QmVTDhiop21CnqyerkcPdC4bCiSH74fXqMAjwwrhgG1omr",
    },
    "Cry Havoc #0045": {
        "ipfs": "QmWFqW6K1PpiR4SawVh4HrBFQNH91CwDvDa7u9j87qcPWX",
    },
    "Cry Havoc #0142": {
        "ipfs": "Qmbn6YgZHygUREZEhWLTXatbiTbmxKuVDMT8tHjxfwyCKp",
    },
    "Dr Jekyll #2291": {
        "ipfs": "Qmazkd2b4WmrHA6H5M3xkH1d4uGyT8vCHvPD6C92E3gyQY",
    },
    "Heart of a Dragon #600": {
        "ipfs": "QmaRGBCRvhsPaLxejjuHeuZmmyKGGzyEBrw3GWMWqeAVQB",
        "bonus": [
            " + Cleopatra, a David Niall Wilson NFT token for ",
            "discounts on future minted books from his award-winning titles.",
        ],
    },
    "Heart of a Dragon #952": {
        "ipfs": "QmPGspgmwzrYBasCEXGMgX7VhfWYL9iA9gAd9pHbJFGKvJ",
        "bonus": [
            " + The Brownstone, a David Niall Wilson NFT token for ",
            "discounts on future minted books from his award-winning titles.",
        ],
    },
    "Metal Monster #0246": {
        "ipfs": "QmahjSvaLMa9Yp54nhewTxPJymfgXDywZ1YyCiy4MWqYTX",
    },
    "Metal Monster #2420": {
        "ipfs": "QmX9xFYYdpGQCUp5p1eP53iVcai95nSbqn4T2hKKbgWSdf",
    },
    "Metamorphosis #0330": {
        "ipfs": "QmbVELHTF7zo1XzswjJKujaThhWqmfWHTtpENdsZrrmUPB",
    },
    "Metamorphosis #0627": {
        "ipfs": "QmYV8QDLhhLaJENg8hnKcDdd9r4gkf3cRCqcfEVLbXaUSb",
    },
    "SILVER #0968": {
        "ipfs": "QmbVH2eqqsepbEdb4pgHJL8XRVWYNC8j4eWXQyGxSLB5cB",
    },
    "SILVER #0999": {
        "ipfs": "QmfN1rofENz7tc7bYkCqbPuJ9GGXK25zfEbE2WB1U2YLda",
    },
    "SILVER #1233": {
        "ipfs": "QmR4Fh3yQz4vrWmL6ybYp7Gt6cdy7u18RCcWWq59Kiw5aT",
    },
    "The Kama Sutra #316": {
        "ipfs": "QmVUNWvJMkhsmyvpq2Kp7qX6W7GyBqE6ZdqZ4HuPZuY4cc",
    },
    "The Wizard Tim #1856": {
        "ipfs": "QmcALqJTGokH7ANgQyfgNJ1FbK6uhQk1Ur7ZoDAznn532m",
    },
    "The Wizard Tim #1947": {
        "ipfs": "QmaFThUML6MrVnoQNAezyu9cfkr2PjRXwV3pvZW2USaZ3g",
    },
    "To The Vanishing Point #0498": {
        "ipfs": "Qme6kiyJBdsvtpmpYZ32FecLxDNLdnw9nRjJh6tZ45LmTC",
    },
    "Treasure Island #0924": {
        "ipfs": "QmceoeiFkz7GEmbSDXDfi7EsKUinLBoJYEuKQDBxATdjBx",
    },
    "Treasure Island #1088": {
        "ipfs": "QmWrjYCaTrzWNQWUqqiFy2EKx13ySTaBr1AgNzS3ecWBPq",
    },
    "Twenty Thousand Leagues #0970": {
        "ipfs": "QmW33vvk2eUcBeG8opCxfEBpyJX1mNPY1vKSFydRPS7tdc",
    },
    "Twenty Thousand Leagues #1709": {
        "ipfs": "QmPJWpsNtLPXwLGD8stfchp1GTN4iQktZDFMz3ERyxD63A",
    },
    "Twenty Thousand Leagues #2284": {
        "ipfs": "QmcnXebVSayQ85eTk2Lf8knqpqYrCqgwtZSyn5iPouNdwL",
    },
    "Twenty Thousand Leagues #2507": {
        "ipfs": "QmYCCF6oNDnAx52Epj1NHs3pFbDLnUvQn3TNcJ4rzBeNTF",
    },
}


toolkit.generate_metadata(
    POLICY_ID,
    normal_ipfs=NORMAL_IPFS,
    normal_supply=NORMAL_SUPPLY,
    goldens=GOLDENS,
    make_zip=False,
)
