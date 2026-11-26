import subprocess
import os

def jalankan_git(perintah):
    hasil = subprocess.run(
        perintah,
        capture_output=True,
        text=True
    )

    if hasil.returncode != 0:
        print("Terjadi kesalahan:")
        print(hasil.stderr)
        return False

    print(hasil.stdout)
    return True


def push_github():
    print("=== AUTO PUSH GITHUB ===")

    if not os.path.isdir(".git"):
        print("Folder bukan repository Git!")
        return

    print("\nMenambahkan perubahan...")
    if not jalankan_git(["git", "add", "-A"]):
        return

    hasil = subprocess.run(
        ["git", "diff", "--cached", "--quiet"]
    )

    if hasil.returncode == 0:
        print("Tidak ada perubahan baru.")
        return

    pesan = input("\nMasukkan pesan commit: ")

    if not pesan.strip():
        print("Pesan commit tidak boleh kosong!")
        return

    print("\nMelakukan commit...")
    if not jalankan_git(["git", "commit", "-m", pesan]):
        return

    print("\nMengirim ke GitHub...")
    if not jalankan_git(["git", "push", "origin", "main"]):
        return

    print("\nPUSH BERHASIL! File sudah dikirim ke GitHub.")


push_github()