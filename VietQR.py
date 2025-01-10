bank_list = [
    app_commands.Choice(name="Vietcombank", value="vcb/123456789"),
]
async def `command_name` (interaction: discord.Interaction, bank: app_commands.Choice[str], amount: str, description: str):
    try:
        if not amount.strip():
            raise ValueError("Không được để trống.")
        if "k" in amount.lower():
            amount = amount.lower().replace("k", "")
            if not amount.isdigit():
                raise ValueError("Không hợp lệ.")
            amount = int(amount) * 1000
        else:
            if not amount.isdigit():
                raise ValueError("Không hợp lệ.")
            amount = int(amount)
        
        bank_code, bank_account = bank.value.split("/")
        description = description.strip() or "Không có nội dung"
        
        encoded_description = urllib.parse.quote(description)
        encoded_account_name, account_name = urllib.parse.quote("Nguyen Van A")
        qr_url = (
            f"https://img.vietqr.io/image/{bank_code}-{bank_account}-compact.png"
            f"?amount={amount}&addInfo={encoded_description}&accountName={encoded_account_name}"
        )

        embed = discord.Embed(
            title="Thông tin thanh toán",
            color=discord.Color.blue()  
        )
        embed.add_field(name="Ngân Hàng:", value=f"```{bank.name}```", inline=False)
        embed.add_field(name="Số Tài Khoản:", value=f"```{bank_account}```", inline=False)
        embed.add_field(name="Chủ Tài Khoản:", value=f"```{account_name}```", inline=False)  # Replace with actual account holder name if available
        embed.add_field(name="Số Tiền:", value=f"```{amount:,} VNĐ```", inline=False)
        embed.add_field(name="Nội Dung:", value=f"```{description}```", inline=False)
        embed.set_footer(text="Made by KeThienIT", icon_url=interaction.user.avatar.url)
        embed.set_thumbnail(url=interaction.user.avatar.url) 
        embed.set_image(url=qr_url)
        
        await interaction.response.send_message(embed=embed, ephemeral=False)
