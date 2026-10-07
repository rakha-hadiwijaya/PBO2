<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('insidens', function (Blueprint $table) {
            $table->id();
            $table->foreignId('site_id')->constrained()->cascadeOnDelete();
            $table->foreignId('pegawai_id')->nullable()->constrained()->nullOnDelete();
            $table->date('tanggal');
            $table->enum('jenis_insiden', ['Near Miss', 'Kecelakaan Kerja', 'Kerusakan Alat']);
            $table->enum('tingkat_keparahan', ['Ringan', 'Sedang', 'Berat', 'Fatal']);
            $table->text('deskripsi')->nullable();
            $table->text('tindakan')->nullable();
            $table->enum('status', ['Terbuka', 'Investigasi', 'Selesai']);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('insidens');
    }
};
