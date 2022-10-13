import asyncio
from carbon import Carbon

client = Carbon()


async def get_carbon_image(code: str) -> str:
    """
    Purpose:
        Create carbon file
    Args/Requests:
         code: code to carbonize
    Return:
        file_path: loc of carbon file
    """
    img = await client.create(code)
    return img


# code = """
# pragma solidity ^0.8.0;

# import "./ERC721Tradable.sol";

# /**
#  * @title GitNFT
#  * GitNFT - a contract for code GitNFTs.
#  */
# contract GitNFT is ERC721Tradable {
#     uint256 public nextTokenId;
#     address public admin;

#     constructor(address _proxyRegistryAddress)
#         public
#         ERC721Tradable("GitNFT", "GitNFT", _proxyRegistryAddress)
#     {
#         admin = msg.sender;
#     }

#     // only our wallet should be able to mint
#     function mint(address to) external onlyOwner {
#         _safeMint(to, nextTokenId);
#         nextTokenId++;
#     }

#     function baseTokenURI() public pure override returns (string memory) {
#         return "https://www.gitgallery.com/tokenid/";
#     }
# }
# """
code = 'pragma solidity ^0.8.0;\n\nimport "./ERC721Tradable.sol";\n\n/**\n * @title GitNFT\n * GitNFT - a contract for code GitNFTs.\n */\ncontract GitNFT is ERC721Tradable {\n    uint256 public nextTokenId;\n    address public admin;\n\n    constructor(address _proxyRegistryAddress)\n        public\n        ERC721Tradable("GitNFT", "GitNFT", _proxyRegistryAddress)\n    {\n        admin = msg.sender;\n    }\n\n    // only our wallet should be able to mint\n    function mint(address to) external onlyOwner {\n        _safeMint(to, nextTokenId);\n        nextTokenId++;\n    }\n\n    function baseTokenURI() public pure override returns (string memory) {\n        return "https://www.gitgallery.com/tokenid/";\n    }\n}\n'


async def main():
    img = await client.create(code)
    print(img)


asyncio.run(main())
